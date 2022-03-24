import pytest

import autodsc.utils.sklearn


@pytest.fixture
def print_changed_only_false():
    sklearn.set_config(print_changed_only=False)
    yield
    sklearn.set_config(print_changed_only=True)  # reset to default
