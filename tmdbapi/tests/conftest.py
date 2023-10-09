import shutil
from pathlib import Path

import pytest

# @pytest.fixture(autouse=True)
# def run_before_and_after_tests(tmpdir):
#     """Fixture to execute before and after tests is run"""
#     # setup before tests
#     Path("tmdbapi/tests/temp").mkdir(parents=True, exist_ok=True)

#     yield # running the tests

#     # clean up after tests
#     shutil.rmtree("tmdbapi/tests/temp", ignore_errors=True)


def pytest_addoption(parser):
    """An command line option to specify credential file"""
    parser.addoption(
        "--cred",
        action="store",
        help="Specify the path to the credential file",
        type=Path,
    )


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    try:
        path = config.getoption("--cred")
    except:
        path = None
    if path is None:
        cred_path = Path("test.credential")
    else:
        cred_path = path
    if cred_path.is_file():
        path_text = cred_path.absolute()
    else:
        raise FileNotFoundError(f"Not found: {cred_path.absolute()}")

    Path("tmdbapi/tests/temp").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path_text, "tmdbapi/tests/temp/test.credential")


def pytest_unconfigure():
    """Clean up at the end of test"""
    shutil.rmtree("tmdbapi/tests/temp", ignore_errors=True)


class DataSharing:
    id = None
