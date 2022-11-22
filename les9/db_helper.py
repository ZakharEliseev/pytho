URL_DEFAULT = 'sqlite://'


class Engine:
    def __init__(self, url):
        self.url = url


class Connection:
    def __init__(self, engine):
        self.engine = engine


def get_engine(url=None):
    return Engine(url or URL_DEFAULT)


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(Engine)
