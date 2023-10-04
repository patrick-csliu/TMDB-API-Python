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


LANGUAGE = "en-US"
PERSON_ID = 31


def test_changes():
    tmdbapi.api3.people.changes(PERSON_ID, "2020-01-01", "2020-01-10")


def test_combined_credits():
    tmdbapi.api3.people.combined_credits(PERSON_ID, LANGUAGE)


def test_details():
    tmdbapi.api3.people.details(PERSON_ID, language=LANGUAGE)


def test_external_ids():
    tmdbapi.api3.people.external_ids(PERSON_ID)


def test_images():
    tmdbapi.api3.people.images(PERSON_ID)


def test_latest():
    tmdbapi.api3.people.latest()


def test_movie_credits():
    tmdbapi.api3.people.movie_credits(PERSON_ID, LANGUAGE)


def test_popular():
    tmdbapi.api3.people.popular(PERSON_ID, LANGUAGE)


def test_tagged_images():
    tmdbapi.api3.people.tagged_images(PERSON_ID)


def test_translations():
    tmdbapi.api3.people.translations(PERSON_ID)


def test_tv_credits():
    tmdbapi.api3.people.tv_credits(PERSON_ID, LANGUAGE)
