#!/usr/bin/python3

class Users():
    """Класс пользователей, login, logout, и подсчёт кол-ва входов"""

    def __init__(
            self, name,
            login):
        """Стандартные параметры пользователя

        Принимает:
            self - стандартное имя первого аргумента для методов объекта
            name - параметр имени пользователя
            login - параметр логина пользователя
        """
        self.name = name
        self.login = login

        # Кол-во входов пользователя по умолчанию:
        self.login_count = 0

    def info(self):
        """Имя, логин и количество входов по-умолчанию у пользователей.

        Принимает:
            self - стандартное имя первого аргумента для методов объекта.
        Возвращает:
            Полную информацию по пользователю,
            его имя, логин и количество входов по-умолчанию.
        """
        site = (f'Имя пользователя: {self.name} Логин пользователя: {self.login} Количество входов пользователя: {str(self.login_count)}')
        print(f'{site}')

    def logon(self):
        """Метод, с помощью которого пользователи
        входят в систему с счётчиком входов

        Принимает:
            self - стандартное имя первого аргумента для методов объекта.
        Возвращает:
            Сообщение о том что пользователей
            с таким-то логином и именем вошёл в систему.
            Если он входит в систему первый раз,
            так же появится соотвествующее сообщение.
        """
        print(f'{self.name}({self.login}) Вошел(ла) в систему')
        self.login_count += 1
        if self.login_count == 1:
            # Если условие истинно (счётчик = 1)
            # выполняем следующий вывод:
            print(f'{self.login} входит в систему первый раз')

    def log_count(self):
        """Метод вывода кол-ва входов всех пользователей

        Принимает:
            self - стандартное имя первого аргумента для методов объекта.
        Возвращает:
            Логин пользователя и общий подсчёт
            количества входов в систему у пользователя.
        """
        print(f'{self.login} входил(а) в систему: {str(self.login_count)} раз(а)')

    def logout(self):
        """Метод, с помощью которого пользователи выходят из системы

        Принимает:
            self - стандартное имя первого аргумента для методов объекта.
        Возвращает:
            Сообщение о том что пользователей
            с таким-то логином и именем вышел из системы.
        """
        print(f'{self.name} ({self.login}) вышел(ла) из системы')

# Создаём экземпляры класса:


user1 = Users("Саня", "Sanya123")
user2 = Users("Вика", "Viktoria88qw")
user3 = Users("Олег", "GoodWorkOleg228")
user4 = Users("Никита Ушинский", "cosnilex")

# Начинаем вызывать различные методы у разных экземпляров класса:


user1.info()
user1.logon()
user1.logout()
print("")
user2.logon()
user2.logout()
print('')
user3.logon()
user3.logout()
print('')
user3.logon()
user3.logout()
print('')
user1.logon()
user1.logout()
user1.logon()
user1.logout()
user1.logon()
user1.logout()
user1.logon()
user1.logout()
user1.logon()
print('')

user4.logon()
user4.logout()
print('')

user2.logon()
user2.logout()
user3.logon()
user3.logout()
print("")
print(f'"Информация по входам пользователей сайта за день: "')
user1.log_count()
user2.log_count()
user3.log_count()
user4.log_count()
print('')
