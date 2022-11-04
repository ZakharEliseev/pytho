class Shape:

    def get_area(self):
        print('not enough data')


class Rectangle(Shape):
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_p(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return f'{self.__class__.__name__}(a={self.a}, b={self.b})'

    def __len__(self):
        return self.get_p()


class Square(Rectangle):
    def __init__(self, a):
        # super().__init__(a, a)
        self.a = a
        # self.b = a

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        self.a = value

rectangle1 = Rectangle(3, 5)

print(rectangle1)
print('p:', len(rectangle1))
print('p:', rectangle1.__len__())
print(rectangle1.get_area())

print("________________________________________________________________")
s1 = Square(6)
print(f's1={s1.a}')
print('p', s1.get_p())
print('sq', s1.get_area())
print("________________________________________________________________")
s1.a = 7
print(f's1={s1.a}, s2={s1.b}')
print('p', s1.get_p())
print('sq', s1.get_area())
print("________________________________________________________________")
s1.b = 8
print(f's1={s1.a}, s2={s1.b}')
print('p', s1.get_p())
print('sq', s1.get_area())