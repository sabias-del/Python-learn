zoo = ("питон", "пингвин", "тюлень") #Помните, что скобки не обязательны.
print('Количество животных в зоопарке - ', len(zoo)) #Печать списка команду Len.
new_zoo = 'Обезьяна', "верблюд" , zoo
print('Количество клеток в зоопарке', new_zoo)
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезенные из старого зоопарке:', new_zoo[2])
print('Последние животное, привезенное из старого зоопарка - ',new_zoo[2][2])
print('Количество животных в новом зоопарке - ',len(new_zoo)-1 + \
      len(new_zoo[2]))