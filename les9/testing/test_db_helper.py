from string import ascii_lowercase
from random import choices, randint, choice

import pytest

from db_helper import (
    Engine,
    Connection,
    get_engine,
    get_connection,
    User,
)


@pytest.fixture
def conn_url():
    return "conn_url"


@pytest.fixture
def engine_default(conn_url) -> Engine:
    return get_engine(url=conn_url)


@pytest.fixture
def connection_default(engine_default) -> Connection:
    return get_connection(engine_default)


def test_fixtures_connection(connection_default, engine_default, conn_url):
    assert isinstance(connection_default, Connection)
    assert isinstance(engine_default, Engine)
    assert connection_default.engine is engine_default
    assert engine_default.url == conn_url


@pytest.fixture
def user():
    username = "".join(choices(ascii_lowercase, k=8))
    user = User(username)
    print("created user", user)
    yield user

    user.delete()


class TestUser:
    def test_set_age(self, user):
        age = randint(1, 100)
        assert user.age != age
        user.set_age(age)
        assert user.age == age
