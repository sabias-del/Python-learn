import random


def guessing_game():
    count_q = 0
    random_int = random.randint(0, 10)

    while True:
        try:
            ask = int(input(f"Hello try to play random int choose: "))
            print(ask)
            # print(random_int)
            if count_q == 3:
                print('Sorry this all.')
                break
            if ask > random_int:
                print("Try less number :)")
                count_q = count_q + 1
                print(f'Your count :{count_q}')
            elif ask < random_int:
                print("Try more number :(")
                count_q = count_q + 1
                print(f'Your count :{count_q}')
            else:
                print("woo you the best!!!")
                break
        except ValueError:
            print("No text only numbers!")


def main():
    guessing_game()


if __name__ == '__main__':
    main()
