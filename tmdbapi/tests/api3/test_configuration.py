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


def test_countries():
    tmdbapi.api3.configuration.countries("zh-TW")


def test_details():
    tmdbapi.api3.configuration.details()


def test_jobs():
    tmdbapi.api3.configuration.jobs()


def test_languages():
    tmdbapi.api3.configuration.languages()


def test_primary_translations():
    tmdbapi.api3.configuration.primary_translations()


def test_timezones():
    tmdbapi.api3.configuration.timezones()
