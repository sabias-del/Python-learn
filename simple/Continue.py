while True:
    s = input('Введите что-нибудь :')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины')  # Разные другие действия здесь...
