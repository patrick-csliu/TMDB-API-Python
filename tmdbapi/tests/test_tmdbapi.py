import os
import sys
from pathlib import Path

import pytest

import tmdbapi

CREDENTIAL_PATH_S = "tmdbapi/tests/temp/test0"
CREDENTIAL_PATH_L = "tmdbapi/tests/temp/test0.credential"
ENC_CREDENTIAL_PATH_S = "tmdbapi/tests/temp/test1"
ENC_CREDENTIAL_PATH_L = "tmdbapi/tests/temp/test1.enc.credential"


@pytest.fixture(autouse=True)
def reload_package():
    # delete all modules from package
    loaded_package_modules = [
        key for key, value in sys.modules.items() if "tmdbapi" in str(value)
    ]
    for key in loaded_package_modules:
        del sys.modules[key]
    global tmdbapi  # reach the global scope
    import tmdbapi  # reimport package every before test

    yield  # run test


class TestCredentials:
    def test_getitem(self):
        cred = tmdbapi.Credential()
        cred.set('1', '2', '3', 4, '5')
        assert cred["api_key"] == '2'

    def test_set_credentials(self):
        cred = tmdbapi.Credential()
        cred.set(
            "test-access-token",
            "test-api-key",
            "test-session-id",
            "test-account-id",
            "test-account-object-id",
        )
        assert cred == {
            "access_token": "test-access-token",
            "api_key": "test-api-key",
            "session_id": "test-session-id",
            "account_id": "test-account-id",
            "account_object_id": "test-account-object-id",
        }

    def test_set_credentials_overwrite_true(self):
        cred = tmdbapi.Credential()
        cred.set('1', '2', '3', 4, '5')
        cred.set('', '', '5', 0, '', overwrite=True)
        assert cred == {
            "access_token": "",
            "api_key": "",
            "session_id": "5",
            "account_id": 0,
            "account_object_id": "",
        }

    def test_set_credentials_overwrite_false(self):
        cred = tmdbapi.Credential()
        cred.set('1', '2', '3', 4, '5')
        cred.set('', '', '5', 0, '', overwrite=False)
        assert cred == {
            "access_token": "1",
            "api_key": "2",
            "session_id": "5",
            "account_id": 4,
            "account_object_id": "5",
        }

    # def test_pytest_scope(self):
    #     cred = tmdbapi.Credential()
    #     assert cred == {
    #         "access_token": "test-access-token",
    #         "api_key": "test-api-key",
    #         "session_id": "test-session-id",
    #         "account_id": "test-account-id",
    #         "account_object_id": "test-account-object-id",
    #     }

    def test_save_credentials(self):
        cred = tmdbapi.Credential()
        cred.set("1", "2", "3", 4, "5")
        cred.save(CREDENTIAL_PATH_S)
        assert Path(CREDENTIAL_PATH_L).exists()

    def test_load_credentials(self):
        cred = tmdbapi.Credential()
        cred.load(CREDENTIAL_PATH_L)
        assert cred == {
            "access_token": "1",
            "api_key": "2",
            "session_id": "3",
            "account_id": 4,
            "account_object_id": "5",
        }

    def test_load_credentials_auto_update_true(self):
        cred = tmdbapi.Credential()
        cred.set("1", "2", "3", 4, "5")
        cred.save(CREDENTIAL_PATH_S, auto_update=True)
        cred.set("2", "3", "4", 5, "6")
        cred2 = tmdbapi.Credential()
        cred2.load(CREDENTIAL_PATH_L)
        assert cred2 == {
            "access_token": "2",
            "api_key": "3",
            "session_id": "4",
            "account_id": 5,
            "account_object_id": "6",
        }

    def test_load_credentials_auto_update_false(self):
        cred = tmdbapi.Credential()
        cred.set("1", "2", "3", 4, "5")
        cred.save(CREDENTIAL_PATH_S, auto_update=False)
        cred.set("2", "3", "4", 5, "6")
        cred2 = tmdbapi.Credential()
        cred2.load(CREDENTIAL_PATH_L)
        assert cred2 == {
            "access_token": "1",
            "api_key": "2",
            "session_id": "3",
            "account_id": 4,
            "account_object_id": "5",
        }

    def test_set_env_var(self):
        cred = tmdbapi.Credential()
        cred.load(CREDENTIAL_PATH_L)
        cred.cred_to_env()
        vars = [
            "TMDB_ACCESS_TOKEN",
            "TMDB_API_KEY",
            "TMDB_SESSION_ID",
            "TMDB_ACCOUNT_ID",
            "TMDB_ACCOUNT_OBJECT_ID",
        ]
        for v, n in zip(vars, ["1", "2", "3", "4", "5"]):
            pytest.assume(os.environ.get(v) == n)

    def test_load_env_var(self):
        cred = tmdbapi.Credential()
        cred.load(CREDENTIAL_PATH_L)
        cred.cred_to_env()
        cred2 = tmdbapi.Credential()
        cred2.load_env_var()
        assert cred2 == {
            "access_token": "1",
            "api_key": "2",
            "session_id": "3",
            "account_id": 4,
            "account_object_id": "5",
        }

    def test_pass_check1(self):
        cred = tmdbapi.Credential()
        assert cred.pass_check()

    def test_pass_check2(self):
        cred = tmdbapi.Credential()
        cred.set("1", "2", "3", 4, "5")
        assert cred.pass_check("access_token", "account_id")

    def test_pass_check3(self):
        cred = tmdbapi.Credential()
        cred.set("1", "2", "3", 0, "5")
        assert not cred.pass_check("access_token", "account_id")
    
    def test_encrypt(self):
        cred = tmdbapi.Credential()
        cred.set("1", "2", "3", 4, "5")
        cred.password = 'test!PaSsWoRd'
        cred.save_encrypt(ENC_CREDENTIAL_PATH_S)
        cred.set("q")
        cred2 = tmdbapi.Credential()
        cred2.password = 'test!PaSsWoRd'
        cred2.load_encrypt(ENC_CREDENTIAL_PATH_L)
        assert cred2 == {
            "access_token": "q",
            "api_key": "2",
            "session_id": "3",
            "account_id": 4,
            "account_object_id": "5",
        }



class TestSettings:
    def test_default(self):
        assert tmdbapi.setting == {
            "use_access_token": False,
            "timeout": None,
            "default_language": None,
            "default_region": None,
            "use_session": False,
            "log_file": None,
            "credential": None,
        }

    def test_error(self):
        with pytest.raises(KeyError):
            tmdbapi.setting.set(wrong_name=True)

    def test_use_access_token1(self):
        cred = tmdbapi.Credential()
        cred.set("1")
        tmdbapi.setting.use_cred(cred)
        tmdbapi.setting.set(use_access_token=True)
        assert tmdbapi.setting["use_access_token"] == True

    def test_use_access_token2(self):
        cred = tmdbapi.Credential()
        tmdbapi.setting.use_cred(cred)
        tmdbapi.setting.set(use_access_token=True)
        assert tmdbapi.setting["use_access_token"] == False
    
    def test_default_language(self):
        tmdbapi.setting.language("zh-TW")
        assert tmdbapi.setting["default_language"] == "zh-TW"

    def test_use_session(self):
        import requests

        tmdbapi.setting.set(use_session=True)
        pytest.assume(tmdbapi.setting["use_session"] == True)
        pytest.assume(isinstance(tmdbapi._SESSION, requests.Session))
        tmdbapi.setting.set(use_session=False)
        pytest.assume(tmdbapi._SESSION is None)

    def test_log_file(self):
        import logging

        tmdbapi.setting.set(log_file="tmdbapi/tests/temp")
        logger = logging.getLogger("TMDB")
        logger.critical("test message")
        pytest.assume(Path("tmdbapi/tests/temp/TMDB.log").exists())
        tmdbapi.setting.set(log_file=None)
        pytest.assume(len(logger.handlers) == 1)
    
    def test_use_cred(self):
        cred = tmdbapi.Credential()
        tmdbapi.setting.use_cred(cred)
        assert isinstance(tmdbapi.setting["credential"], tmdbapi.creds.Credential)

    def test_use_cred_ref1(self):
        cred = tmdbapi.Credential()
        tmdbapi.setting.use_cred(cred)
        cred.set(session_id="q")
        assert tmdbapi.setting["credential"]["session_id"] == "q"

    def test_use_cred_ref2(self):
        cred = tmdbapi.Credential()
        tmdbapi.setting.use_cred(cred)
        c = tmdbapi.setting["credential"]
        c.set(session_id="q")
        assert cred["session_id"] == "q"
