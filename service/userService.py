from dao.userDAO import UserDAO
from model.user import User
from dto.userDto import UserDto, UserUpdateDto


class UserService(object):
    __dao = None

    def __init__(self):
        self.__dao = UserDAO()

    def find_all(self):
        rows = self.__dao.find_all()
        return [UserDto(*row) for row in rows]

    def find_by_id(self, user_id):
        row = self.__dao.find_by_id(user_id)
        return UserDto(*row)

    def add(self, user: UserUpdateDto):
        user_entity = User(id=None, username=user.username, address=user.address, phone=user.phone)
        row = self.__dao.create(user_entity)
        return UserDto(*row)

    def update(self, user_id, user: UserUpdateDto):
        user_entity = User(id=user_id, username=user.username, address=user.address, phone=user.phone)
        row = self.__dao.update(user_entity)
        return UserDto(*row)

    def delete(self, user_id: int):
        self.__dao.delete(user_id)

