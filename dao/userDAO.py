import sqlite3
from model.user import User


class UserDAO(object):
    __db = None

    def __init__(self):
        self.__db = "mydatabase.db"

    def find_all(self):
        with sqlite3.connect(self.__db) as conn:
            cursor = conn.cursor()
            sql = """
                SELECT * from users
            """
            cursor.execute(sql)
            conn.commit()
            rows = cursor.fetchall()
            cursor.close()
            return rows

    def find_by_id(self, user_id):
        with sqlite3.connect(self.__db) as conn:
            cursor = conn.cursor()
            sql = """
                SELECT * from users where id=?
            """
            print(user_id)
            cursor.execute(sql, (user_id,))
            conn.commit()
            row = cursor.fetchone()
            cursor.close()
            return row

    def create(self, user: User):
        with sqlite3.connect(self.__db) as conn:
            cursor = conn.cursor()
            sql = """
                insert into users (username, address,
            phone) values (?,?,?)
            """
            cursor.execute(sql, (user.username, user.address, user.phone))
            user_id = cursor.lastrowid
            print(user_id)
            conn.commit()
            cursor.close()
            return self.find_by_id(user_id)

    def update(self, user: User):
        with sqlite3.connect(self.__db) as conn:
            cursor = conn.cursor()
            sql = """
                update users set username=?, address=?,
                phone=? where id=?
            """
            cursor.execute(sql, (user.username, user.address, user.phone, user.id))
            conn.commit()
            cursor.close()
            return self.find_by_id(user.id)

    def delete(self, user_id):
        with sqlite3.connect(self.__db) as conn:
            cursor = conn.cursor()
            sql = """
                delete from users where id=?
            """
            cursor.execute(sql, (user_id,))
            conn.commit()
            cursor.close()
