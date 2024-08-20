from pythonpipelinedemo.main import add_one
import sys
from packaging import version


def test_main():
    assert add_one(1) == 2


def test_specific_python_version():
    current_version = sys.version.split(" ")[0]
    min_version = "3.12.0"

    # Assert that the current Python version is greater than the minimum required version
    assert version.parse(current_version) > version.parse(
        min_version
    ), f"Python version must be greater than {min_version}. Current version: {current_version}"
