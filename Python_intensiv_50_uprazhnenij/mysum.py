def mysuma(*numbers):
    output = 0
    for numb in numbers:
        output += numb
    return output


def main():
    print(mysuma(10, 20, 30, 40))


if __name__ == '__main__':
    main()
