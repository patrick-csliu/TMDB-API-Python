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
    parser.addoption(
        "--cred",
        action="store",
        help="Specify the path to the credential file",
        type=Path,
    )


# @pytest.fixture
# def credential_path(request) -> str:
#     path = request.config.getoption("--cred")
#     # pyth = pytest.Config().getoption("--cred")
#     if path is None:
#         return Path("test.credential").absolute()
#     else:
#         return path.absolute()


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    path = config.getoption("--cred")
    if path is None:
        cred_path =  Path("test.credential").absolute()
    else:
        cred_path =  path.absolute()
    print(cred_path)
    # print("!!!!!!!!!!!!!!!!!!", type(credential_path), credential_path)
    Path("tmdbapi/tests/temp").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(cred_path, "tmdbapi/tests/temp/test.credential")


def pytest_unconfigure():
    shutil.rmtree("tmdbapi/tests/temp", ignore_errors=True)


class DataSharing:
    id = None
