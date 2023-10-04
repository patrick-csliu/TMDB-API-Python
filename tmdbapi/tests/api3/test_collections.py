import sys

import tmdbapi

TEST = [87359, "zh-TW"]


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


def test_details():
    tmdbapi.api3.collections.details(*TEST)


def test_images():
    tmdbapi.api3.collections.images(TEST[0], include_image_language="zh-TW")


def test_translations():
    tmdbapi.api3.collections.translations(TEST[0])
