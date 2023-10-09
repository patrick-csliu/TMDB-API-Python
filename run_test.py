# Build the package
# And run  pytest

import os
import shutil
import subprocess
import sys
import tempfile
import tomllib
import re

from virtualenv import cli_run

venv_name = "test-venv"
test_requirements = "requirements.txt"


def in_virtualenv():
    def get_base_prefix_compat():
        """Get base/real prefix, or sys.prefix if there is none."""
        return (
            getattr(sys, "base_prefix", None)
            or getattr(sys, "real_prefix", None)
            or sys.prefix
        )

    return sys.prefix != get_base_prefix_compat()


def main():
    # build python
    subprocess.run(["pip", "install", "build"])
    subprocess.run(["python", "-m", "build"])

    # create a test environment
    with open("pyproject.toml", "rb") as f:
        parsed_toml = tomllib.load(f)
    version = parsed_toml["project"]["version"][1:]
    sdist = f"dist/TMDB-Py-{version}.tar.gz"
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=False) as test_dir:
        print("Copy files ...")
        shutil.copy(sdist, test_dir)
        shutil.copy(test_requirements, test_dir)
        shutil.copy("test.credential", test_dir)
        shutil.copy("pytest.ini", test_dir)
        print("Copy finished")
        os.chdir(test_dir)
        with open("pytest.ini", 'r+') as f:
            new = re.sub("tmdbapi/tests", f"{venv_name}/lib/python3.11/site-packages/tmdbapi/tests", f.read())
            f.seek(0)
            f.write(new)
        print("Modify pytest.ini")
        cli_run([venv_name, "-p", "python3.11"])
        activate_file = f"{venv_name}/bin/activate_this.py"
        exec(open(activate_file).read(), {"__file__": activate_file})

        # build environment and test
        if in_virtualenv():
            subprocess.run(["pip", "install", f"TMDB-Py-{version}.tar.gz"])
            subprocess.run(["pip", "install", "-r", test_requirements])
            subprocess.run(["pytest", "--pyargs", "tmdbapi"])


if __name__ == "__main__":
    main()
