some_object = object()

print(some_object)


def my_func():
    print('hello')


my_func()


class MyObject(object):
    pass


class User(object):
    pass

print(object)
print(MyObject)
print(User)

print('name', __name__)

my_obj = MyObject()
user = User()

print(my_obj)
print(user)

print(User.mro())
print(MyObject.mro())

user.name = 'John'
print(user.name)

user2 = User()
user2.name = 'Sam'
print(user2.name)
print(user.name)