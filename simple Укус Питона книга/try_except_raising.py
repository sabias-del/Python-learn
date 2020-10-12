class ShortInputException(Exception):
    """Пользоветельский класс исключения"""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.lenght = length
        self.atleast = atleast


try:
    text = input("Введите что то: ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # здесь может происходить обычная работа
    else:
        print("Мог бы придумать что то интересней - ", text)
except EOFError:
    print("Ну и чем вы сделали EOF?")
except ShortInputException as ex:
    print('ShortInputException: Длина введенной строки -- {0}; \
          ожидалось, как минимум, {1}'.format(ex.lenght, ex.atleast))
