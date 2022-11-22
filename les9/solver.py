class Solver:
    exc_text = 'values should be nums'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        # return 7
        return self.a + self.b

    def mul(self):
        if not all((
            isinstance(self.a, (int, float)),
            isinstance(self.b, (int, float))
        )):
            raise TypeError(self.exc_text)
        return self.a * self.b


def div(a, b):
    return a / b
