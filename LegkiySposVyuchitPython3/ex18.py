# Похоже на сценарий с argv
def print_two(*args):
    args1, args2 = args
    print(f'args1: {args1}, args2: {args2}')

# ок здесь вместо *argv мы делаем следующее

def print_two_again(args1, args2):
    print(f'args1: {args1}, args2: {args2}')

# принемают только один аргумент
def print_one(arg1):
    print(f'arg1: {arg1}')

# не принимает аргументов
def print_none():
    print('А я ничего не получаю.')

print_two('Vibo', "Proto")
print_two_again('Vibo', "Proto")
print_one("Первый!")
print_none()