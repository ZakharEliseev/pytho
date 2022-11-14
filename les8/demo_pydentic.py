from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime | None = None
    friends: list[int] = []


def main():
    # print(datetime.now().timestamp())
    options = {
        # 'signup_ts': 1668423167
        'signup_ts': 0,
        'friends': [b"12", 34, '56']
    }
    user = User(id=1, name='John', **options)
    print(user)
    # print(user.__str__())
    print(repr(user))


if __name__ == '__main__':
    main()
