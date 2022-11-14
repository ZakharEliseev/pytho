def a():
    b, c = 1, 2
    # return None
    # return
    return {'b': b, 'c': c}
    # return User(name='John')


print(a())


class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        ...

    def __repr__(self):
        ...

    def __eq__(self, other):
        ...



