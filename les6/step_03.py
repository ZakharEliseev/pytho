class MyError(Exception):
    pass


print(MyError)
print(MyError.mro())
print(repr(MyError('Error')))


raise MyError()
raise MyError('Error')

print('Never')