import shutil
from pathlib import Path

# @pytest.fixture(autouse=True)
# def run_before_and_after_tests(tmpdir):
#     """Fixture to execute before and after tests is run"""
#     # setup before tests
#     Path("tmdbapi/tests/temp").mkdir(parents=True, exist_ok=True)

#     yield # running the tests

#     # clean up after tests
#     shutil.rmtree("tmdbapi/tests/temp", ignore_errors=True)


def pytest_configure():
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    Path("tmdbapi/tests/temp").mkdir(parents=True, exist_ok=True)
    shutil.copyfile("test.credential", "tmdbapi/tests/temp/test.credential")


def pytest_unconfigure():
    shutil.rmtree("tmdbapi/tests/temp", ignore_errors=True)


class DataSharing:
    id = None
