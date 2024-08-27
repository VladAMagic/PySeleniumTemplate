from dataclasses import dataclass
from typing import Optional


@dataclass
class UserModel:
    id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    username: str
    password: str
