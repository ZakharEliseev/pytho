import pytest


from db_helper import (
    Engine,
    Connection,
    get_connection,
    get_engine
)


@pytest.fixture
def conn_url():
    return 'conn_url'


@pytest.fixture
def engine_default() -> Engine:
    return get_engine(url=conn_url)


@pytest.fixture
def connection_default(engine_default) -> Connection:
    return get_connection(engine_default)


def text_fixtures_connection(engine_default, connection_default, conn_url):
    assert isinstance(connection_default, Connection)
    assert isinstance(engine_default, Engine)
    assert connection_default.engine is engine_default
    assert engine_default.url == conn_url
