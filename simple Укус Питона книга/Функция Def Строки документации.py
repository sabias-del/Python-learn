def printMax(x, y):
    '''Выводит макстмалбное значение двух чисел.
    Оба значения должны быть целыми.'''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'наибольшое')
    else:
        print(y, 'наибольшое')


printMax(3, 5)
print(printMax.__doc__)
