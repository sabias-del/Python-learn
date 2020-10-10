try:
    text = input("Введите что то: ")
except EOFError:
    print("Ну и чем вы сделали EOF?")
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели{0}'.format(text))
