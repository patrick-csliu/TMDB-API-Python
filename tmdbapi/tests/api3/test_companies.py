import sys

import tmdbapi


def setup_module():
    loaded_package_modules = [
        key for key, value in sys.modules.items() if "tmdbapi" in str(value)
    ]
    for key in loaded_package_modules:
        del sys.modules[key]
    global tmdbapi  # reach the global scope
    import tmdbapi  # reimport package every before test

    cred = tmdbapi.Credential()
    cred.load("tmdbapi/tests/temp/test.credential")
    tmdbapi.setting.use_cred(cred)


COMPANY = 4


def test_alternative_names():
    tmdbapi.api3.companies.alternative_names(COMPANY)


def test_details():
    tmdbapi.api3.companies.details(COMPANY)


def test_images():
    tmdbapi.api3.companies.images(COMPANY)
