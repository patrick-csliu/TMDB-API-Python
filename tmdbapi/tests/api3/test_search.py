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


QUERY = "home+road"
LANGUAGE = "en-US"


def test_collections():
    tmdbapi.api3.search.collections(QUERY, language=LANGUAGE)


def test_companies():
    tmdbapi.api3.search.companies(QUERY)


def test_keywords():
    tmdbapi.api3.search.keywords("home")


def test_movies():
    tmdbapi.api3.search.movies(QUERY, language=LANGUAGE)


def test_multi():
    tmdbapi.api3.search.multi(QUERY, language=LANGUAGE)


def test_person():
    tmdbapi.api3.search.person("eric", language=LANGUAGE)


def test_tv():
    tmdbapi.api3.search.tv(QUERY, language=LANGUAGE)
