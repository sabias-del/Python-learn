people = 20
cats = 30
dogs = 15

if people<cats:
    print(f"Слишком много {cats} чем {people} людей. Мир обречен!")

if people>cats:
    print('Не так много кошек, мир спасен!')
else:
    print('Це не кицька')

if people<dogs:
    if True:
        print('Мир утоп в слюнях!')
else:
    print(f"{people} все еще больше чем, {dogs}")

if people>dogs:
    if not True:
        print(f'{people} людей моглы быть больше, если бы собак не было {dogs} столько.')
    else:
        print(False) or print(people - dogs)

dogs += 5


if people >= dogs:
    if not True:
        print('\tЛюдей больше. \n \tИли столько же сколько собак.')
    else:
        print('\tЛюдей много, собак больше, чем котов.')

if people == dogs:
    if True and people+dogs:
        print(people+dogs)