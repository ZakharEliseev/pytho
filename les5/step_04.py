class Date:
    def __init__(self, year: int, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_date_string(cls, date_string: str):
        '''
        accepts strings loke '2022-11-25'
        :param date_string:
        :return:
        '''
        year, month, day = map(int, date_string.split("-"))
        return cls(year=year, month=month, day=day)

    @staticmethod
    def is_date_string_valid(date_string: str) -> bool:
        if date_string.count('-') != 2:
            return False
        year, month, day = map(int, date_string.split("-"))
        return day <= 31 and month <= 12 and year <= 3999

    def copy(self):
        return self.__class__(
            year=self.year,
            month=self.month,
            day=self.day
        )

    def __str__(self):
        return (f'{self.__class__.__name__}(year={self.year}, '
                f'month={self.month}, day={self.day})'
                )


d1 = Date(2001, 4, 30)
print(f'd1 is: {d1}')
d2 = Date(2002, 2, 22)
print(f'd2 is: {d2}')
print('________________________________________________________________')
d3 = d2
print(f'd2 is: {d2}')
print(f'd3 is: {d3}')
print('________________________________________________________________')
d1.month = 6
d2.year = 2004
d3.day = 5
print(f'd1 is: {d1}')
print(f'd2 is: {d2}')
print(f'd3 is: {d3}')
print('________________________________________________________________')
print(d2 is d3)
print(id(d2))
print(id(d3))
print('________________________________________________________________')
d4 = d3.copy()
print(f'd3 is: {d3}')
print(f'd4 is: {d4}')
print('________________________________________________________________')
print(d4 is d3)
d4.day = 15
d3.year = 2010
print(f'd3 is: {d3}')
print(f'd4 is: {d4}')
print('________________________________________________________________')
# Date.from_date_string(True)
# Date.from_date_string(None)
# Date.from_date_string(123)
# Date.from_date_string({'foo': 'bar'})
# print(Date.from_date_string('foo-bar'))
# print(Date('foo', None, []))
print(Date.from_date_string('2022-11-25'))
print(Date.from_date_string('2000-11-25'))
print(Date.from_date_string('2022-20-42'))
print('________________________________________________________________')
print("check '2022-11-25'", Date.is_date_string_valid('2000-20-42'))
print("check '2022-11-25'", Date.is_date_string_valid('2022-11-25'))
print("check '2022-11-25'", Date.is_date_string_valid('2022-02-31'))
