def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f'У нас есть {cheese_count} сырков!')
    print(f'У нас есть {boxes_of_crackers} пачек чипсов!')
    print('Это достаточно для вечеринки!')
    print('Погнали!\n')

print('Мы можем передать числа функции:')
cheese_and_crackers(30, 20)

print('Или мы можем использовать переменные из нашего сценария: ')
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print('Мы можем даже вычислять внутри функции:')
cheese_and_crackers(30+40, 50+10)

print('И обьединять переменные с вычислениями:')
cheese_and_crackers(amount_of_cheese+50, amount_of_crackers+500)
