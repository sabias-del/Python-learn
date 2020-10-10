x = 50


def func(x):
    print("x равен", x)
    x = 2
    print("Замена локального x на", x)


func(x)
print("x по прежднему", x)

y = 50


def func2():
    global y

    print("y равно", y)
    y = 20
    print("заменяем глобальное значение ", y)


func2()
print("Значение y составляет ", y)
