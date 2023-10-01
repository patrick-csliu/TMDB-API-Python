import os
import sys
from pathlib import Path

import pytest

import tmdbapi

CREDENTIAL_PATH = "tmdbapi/tests/temp/test0.credential"

@pytest.fixture(autouse=True)
def reload_package():
    # delete all modules from package
    loaded_package_modules = [key for key, value in sys.modules.items() if "tmdbapi" in str(value)]
    for key in loaded_package_modules:
        del sys.modules[key]
    global tmdbapi  # reach the global scope
    import tmdbapi  # reimport package every before test
    yield           # run test


class TestCredentials:

    def test_set_credentials(self):
        tmdbapi.credential.set_credentials(
            'test-access-token',
            'test-api-key',
            'test-session-id',
            'test-account-id',
            'test-account-object-id'
            )
        assert tmdbapi.credential.CREDENTIALS == {
            "access_token": 'test-access-token',
            "api_key": 'test-api-key',
            "session_id": 'test-session-id',
            "account_id": 'test-account-id',
            "account_object_id": 'test-account-object-id',
        }

    # def test_pytest_scope(self):
    #     assert tmdbapi.credential.CREDENTIALS == {
    #         "access_token": 'test-access-token',
    #         "api_key": 'test-api-key',
    #         "session_id": 'test-session-id',
    #         "account_id": 'test-account-id',
    #         "account_object_id": 'test-account-object-id',
    #     }

    def test_save_credentials(self):
        tmdbapi.credential.set_credentials('1', '2', '3', 4, '5')
        tmdbapi.save_credentials(CREDENTIAL_PATH)
        assert Path(CREDENTIAL_PATH).exists()

    def test_load_credentials(self):
        tmdbapi.load_credentials(CREDENTIAL_PATH)
        assert tmdbapi.credential.CREDENTIALS == {
            "access_token": '1',
            "api_key": '2',
            "session_id": '3',
            "account_id": 4,
            "account_object_id": '5',
        }

    def test_set_env_var(self):
        tmdbapi.load_credentials(CREDENTIAL_PATH)
        tmdbapi.credential.set_env_var()
        vars = [
            'TMDB_ACCESS_TOKEN',
            'TMDB_API_KEY',
            'TMDB_SESSION_ID',
            'TMDB_ACCOUNT_ID',
            'TMDB_ACCOUNT_OBJECT_ID'
        ]
        for v, n in zip(vars, ['1', '2', '3', '4', '5']):
            pytest.assume(os.environ.get(v) == n)
            
    def test_load_env_var(self):
        tmdbapi.load_credentials(CREDENTIAL_PATH)
        tmdbapi.credential.set_env_var()
        tmdbapi.credential.CREDENTIALS = {}
        tmdbapi.credential.load_env_var()
        assert tmdbapi.credential.CREDENTIALS == {
            "access_token": '1',
            "api_key": '2',
            "session_id": '3',
            "account_id": 4,
            "account_object_id": '5',
        }


class TestSettings:

    def test_default(self):
        assert tmdbapi._core.SETTINGS == {
            "use_access_token": False,
            "timeout": None,
            "default_language": None,
            "default_region": None,
            "use_session": False,
            "log_file": None,
        }

    def test_error(self):
        with pytest.raises(KeyError):
            tmdbapi.settings(wrong_name=True)

    def test_use_access_token1(self):
        tmdbapi.credential.set_credentials(access_token='1')
        tmdbapi.settings(use_access_token=True)
        assert tmdbapi._core.SETTINGS['use_access_token'] == True

    def test_use_access_token2(self):
        tmdbapi.settings(use_access_token=True)
        assert tmdbapi._core.SETTINGS['use_access_token'] == False

    def test_use_session(self):
        import requests
        tmdbapi.settings(use_session=True)
        pytest.assume(tmdbapi._core.SETTINGS['use_session'] == True)
        pytest.assume(isinstance(tmdbapi._core.Tmdb.session, requests.Session))
        tmdbapi.settings(use_session=False)
        pytest.assume(tmdbapi._core.Tmdb.session is None)


    def test_log_file(self):
        import logging
        tmdbapi.settings(log_file="tmdbapi/tests/temp")
        logger = logging.getLogger("TMDB")
        logger.critical('test message')
        pytest.assume(Path("tmdbapi/tests/temp/TMDB.log").exists())
        tmdbapi.settings(log_file=None)
        pytest.assume(len(logger.handlers) == 1)
