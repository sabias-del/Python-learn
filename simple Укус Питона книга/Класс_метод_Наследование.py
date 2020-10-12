from abc import *


class schoolMember(metaclass=ABCMeta):
    """Представляет любого человека в школе"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан schoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        """Вывести информацию."""
        print('(Имя:"{0}" Возраст:"{1}")'.format(self.name, self.age), end="")


class Teacher(schoolMember):
    """Представляет преподователя"""

    def __init__(self, name, age, salary):
        schoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        schoolMember.tell(self)
        print('(Зарплата: "{0:d}")'.format(self.salary))


class student(schoolMember):
    '''Студент университета'''

    def __init__(self, name, age, marks):
        schoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан student: "{0}")'.format(self.name))

    def tell(self):
        schoolMember.tell(self)
        print('(Оценки:"{0:d}")'.format(self.marks))


t = Teacher("Ms. Shian", 40, 30000)
s = student("Jonni AF", 25, 75)
print()

members = [t, s]
for members in members:
    members.tell()  # работает как для преподователя так для студента
