import pytest

from .Faloodeh_Framwork import Faloodeh


@pytest.fixture
def api():
    return Faloodeh()


@pytest.fixture
def client(api):
    return api.test_session()