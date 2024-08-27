from typing import Dict
from faker import Factory
from src.data.model.user import UserModel

from dataclasses import replace
from typing import Optional


def __default_user() -> UserModel:
    fake = Factory.create()
    return UserModel(
        id=fake.uuid4(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        username="demouser\n",
        password="testingisfun99\n",
    )


def create_default_user(overwrites: Dict[str, any] = {}) -> UserModel:
    default_user = __default_user()
    return replace(default_user, **overwrites)
