class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})" # заменяем вывод с <__main__.Point object at
                                                                    # 0x7f387c283ee0> на название класса и значение переменных


p1 = Point(2, 3)
print('p:', p1.x, p1.y)

print('p1:', p1)
print('p1:', str(p1))
