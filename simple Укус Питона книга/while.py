number = 23

running = True

while running:
    guess = int(input("Ведите число: "))

    if guess == number:
        print("Поздравляю Вы Угадали!!!")
        running = False
    elif guess < number:
        print("Холодно, больше !")
    else:
        print("Жарко, меньше !")
else:
    print("end")

print("Завершение")
