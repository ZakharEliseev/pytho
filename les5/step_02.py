class User:
    def __init__(self, name=None, age=None, **kwargs):
        self.name = name
        self.age = age
        print(kwargs)
        self.spam = kwargs.get('spam')


user = User('john', 10)
print(user)
print(user.__dict__)

user_sam = User('sam')
print(user_sam)
print(user_sam.__dict__)

print(user_sam.spam)
u = User('nick', spam='eggs', foo='bar', num=123)
print(u.spam)
