import pytest


@pytest.fixture(scope='session', autouse=True)
def base_url():
    url="https://reqres.in/api/users"