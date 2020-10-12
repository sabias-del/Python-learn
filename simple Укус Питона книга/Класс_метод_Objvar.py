class Robot:
    '''Представляем робота с именем.'''
    # Переменная класса, содержащая количесво роботов.

    population = 0

    def __init__(self, name):
        '''Иницилизация данных'''
        self.name = name
        print('(Иницилизация {0})'.format(self.name))

        # При создание личности робот добавляется к переменной популяции.
        Robot.population += 1

    def __del__(self):
        '''Я умираю'''
        print('{0} был последним.'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось{0:d}работающих роботов.'.format( \
                Robot.population))

    def sayHi(self):
        """Привествие робота
        Да, они могут."""
        print("Приветствую! Мои хозяева называют меня{0}.".format(self.name))

    def howMany():
        """Выводит численность роботов"""
        print("У нас роботов {0:d}.".format(Robot.population))

    howMany = staticmethod(howMany)


droid1 = Robot("Р2-Д2")
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")

del droid1
del droid2

Robot.howMany()
