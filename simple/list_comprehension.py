# Генераторы списков

listone = [2, 3, 4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)


# Передача кортежей и словарей в функции

def powersum(power, *args):
    """Возвращает сумму аргументов, возведённых в указанную степень."""
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 3))
