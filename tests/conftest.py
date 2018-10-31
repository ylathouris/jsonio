
import os
import pytest


@pytest.fixture(scope='session')
def json_path():
    """
    Path to JSON file used for testing.

    Returns:
        str: Path to JSON file used for testing.
    """
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, 'data', 'test.json')
