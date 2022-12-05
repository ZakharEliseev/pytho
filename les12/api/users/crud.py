from dataclasses import dataclass, Field

from .schemes import UserIn, User


@dataclass
class UserStorage:
    counter: int
    by_id: dict[int, User]

    @property
    def next_id(self) -> int:
        self.counter += 1
        return self.counter


storage = UserStorage(counter=0, by_id={})


def get_users() -> list[User]:
    return list(storage.by_id.values())

def get_user_by_id(user_id: int) -> User | None:
    return storage.by_id.get(user_id)


def create_user(user_in: UserIn) -> User:
    user_id = storage.next_id
    user = User(id=user_id, **user_in.dict())
    storage.by_id[user.id] = user
    return user


