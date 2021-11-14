from abc import ABC, abstractmethod
import sqlite3
from sqlite3.dbapi2 import Error, sqlite_version

class Rules:
    SUPER_USER:str = "SUPER_USER"
    SIMPLE_USER:str = "SIMPLE_USER"

class User(ABC):
    """
    Базовый класс пользователя
    """
    def __init__(self, login:str, passw:str) -> None:
        self.login = login
        self.passw = passw

    @abstractmethod
    def get_file() -> None:
        """
        Абстрактный метод на передачу файла
        """
        raise NotImplementedError


    @abstractmethod
    def take_file() -> None:
        """
        Абстрактный метод на приём файла
        """
        raise NotImplementedError

    @abstractmethod
    def get_type_rule(self) -> str:
        """
        Абстрактный метод на выдачу уровнядоступа
        """
        raise NotImplementedError

    def get_data_list() -> None:
        """
        Получаем список файлов
        """
        pass

class Super_user(User):
    def __init__(self, login: str, passw: str) -> None:
        super().__init__(login, passw)

    def get_file() -> None:
        """
        Получить файл и записать его в базу
        """
        print("Записываю файл")

    def get_type_rule(self) -> str:
        return Rules.SUPER_USER

    def take_file() -> None:
        print("Передаю файл")

class User_db:
    def __init__(self, name_db) -> None:
        try:
            self.db = sqlite3.connect(name_db)
        except Error:
            print('Errors with connecting to data base')

        self.sql = self.db.cursor()
        self.sql.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT,
            password TEXT,
            rules TEXT
            )""")
        self.db.commit()

    def insert_user(self, user: User):
        self.sql.execute(f"SELECT login FROM users WHERE login == '{user.login}'")
        if self.sql.fetchone() is None:
            print(f'Created {user.login} user ')
            self.sql.execute(f'INSERT INTO users VALUES (?, ?, ?)',
                            (user.login, user.passw, user.get_type_rule()))
                            
            self.db.commit()
        else:
            print(f'This user {self.sql.fetchone()} is exist')

    def get_users(self, login: str, passw: str):
        self.sql.execute(f"SELECT login FROM users WHERE password = '{passw}' AND login = '{login}'")
        row = self.sql.fetchall()
        if len(row) == 0:
            print(f"Login or passw is not correct")
            raise AssertionError
        else:
            print(f"Get {row[0][0]} user")
            return Super_user(login, passw)
