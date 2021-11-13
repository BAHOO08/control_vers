from abc import ABC, abstractmethod


class User(ABC):
    """
    Базовый класс пользователя
    """
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


    def get_data_list() -> None:
        """
        Получаем список файлов
        """
        pass

class Super_user(User):
    def get_file() -> None:
        """
        Получить файл и записать его в базу
        """
        print("Записываю файл")


    def take_file() -> None:
        print("Передаю файл")