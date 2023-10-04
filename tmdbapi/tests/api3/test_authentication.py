# import sys

# import tmdbapi


# def setup_module():
#     loaded_package_modules = [key for key, value in sys.modules.items() if "tmdbapi" in str(value)]
#     for key in loaded_package_modules:
#         del sys.modules[key]
#     global tmdbapi  # reach the global scope
#     import tmdbapi  # reimport package every before test
#
#     cred = tmdbapi.Credential()
#     cred.load("tmdbapi/tests/temp/test.credential")
#     tmdbapi.setting.use_cred(cred)


# def test_create_guest_session():
#     tmdbapi.api3.authentication.create_guest_session()


# def test_create_request_token():
#     tmdbapi.api3.authentication.create_request_token()


# def test_create_session():
#     tmdbapi.api3.authentication.create_session()


# def test_create_session_from_login():
#     tmdbapi.api3.authentication.create_session_from_login()


# def test_create_session_from_v4_token():
#     tmdbapi.api3.authentication.create_session_from_v4_token()


# def test_delete_session():
#     tmdbapi.api3.authentication.delete_session()


# def test_validate_key():
#     tmdbapi.api3.authentication.validate_key()
