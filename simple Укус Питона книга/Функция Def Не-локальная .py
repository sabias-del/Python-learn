x = 50


def func():
    x = 2
    print("x равен", x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print("Локальное имя сменилось ", x)


func()
