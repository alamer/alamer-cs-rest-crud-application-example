from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class UserDto:
    id: int
    username: str
    address: str
    phone: str


@dataclass_json
@dataclass
class UserUpdateDto:
    username: str
    address: str
    phone: str
