import os
import sys
from pathlib import Path

import pytest

import tmdbapi

CREDENTIAL_PATH = "tmdbapi/tests/temp/test0.credential"


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
        cred.save(CREDENTIAL_PATH)
        assert Path(CREDENTIAL_PATH).exists()

    def test_load_credentials(self):
        cred = tmdbapi.Credential()
        cred.load(CREDENTIAL_PATH)
        assert cred == {
            "access_token": "1",
            "api_key": "2",
            "session_id": "3",
            "account_id": 4,
            "account_object_id": "5",
        }

    def test_set_env_var(self):
        cred = tmdbapi.Credential()
        cred.load(CREDENTIAL_PATH)
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
        cred.load(CREDENTIAL_PATH)
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

    def test_use_session(self):
        import requests

        tmdbapi.setting.set(use_session=True)
        print(tmdbapi.setting["use_session"])
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
