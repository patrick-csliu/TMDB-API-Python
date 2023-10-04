# import sys

# import tmdbapi


# def setup_module():
#     loaded_package_modules = [
#         key for key, value in sys.modules.items() if "tmdbapi" in str(value)
#     ]
#     for key in loaded_package_modules:
#         del sys.modules[key]
#     global tmdbapi  # reach the global scope
#     import tmdbapi  # reimport package every before test

#     cred = tmdbapi.Credential()
#     cred.load("tmdbapi/tests/temp/test.credential")
#     tmdbapi.setting.use_cred(cred)


# def test_create_access_token():
#     tmdbapi.api4.auth.create_access_token()


# def test_create_request_token():
#     tmdbapi.api4.auth.create_request_token()


# def test_logout():
#     tmdbapi.api4.auth.logout()
