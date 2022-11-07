def add(a, b):
    return a + b


print(add(1, 2))
print(add(1, 10))
# print(add(1,'10'))
# c = add(2, '8')
# print(c / 2)

print([1, 2] + [3])


class mylist(list):
    def __add__(self, other):
        if isinstance(other, int):
            other = [other]
        return super().__add__(other)


print(mylist([1, 2]) + 5)
print(mylist([1, 2]) + [3, 4])

# raise print('aaaaaaaaaa', Exception)
raise NameError('Ошибка')
raise Exception('ты не прав, (потому что...)')
print('Never')
