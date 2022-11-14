from dataclasses import dataclass, asdict, field


@dataclass()
# @dataclass()
class User:
    id: int
    name: str
    email: str = None


@dataclass()
class Manager(User):
    users: list = field(default_factory=list)


def get_user_dc() -> User:
    user = User(1, name="John")
    print(user)
    u1 = user

    user2 = User(2, "Sam", 'sam@example.com')
    print(user2)
    user3 = User(3, "Nick", email='nick@example.com')
    print(user3)

    # u1.email = 'user@example.com'
    print(user)
    # print(help(User.__init__))
    # help(User)
    print([u1, user2, user3])

    print(asdict(user3))
    # manager = Manager(asdict(user3),'name')
    u4_1 = User(id=4, name='U4')
    u4_2 = User(**{'id': 4, 'name': 'U4'})
    assert u4_1 == u4_2
    manager = Manager(**asdict(user3))
    print(manager)
    print('user3 == manager: ', manager == user3)
    print(User.__annotations__)


def main():
    get_user_dc()


if __name__ == '__main__':
    main()
