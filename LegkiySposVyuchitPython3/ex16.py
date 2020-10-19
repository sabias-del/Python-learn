from sys import argv

script, filename = argv
print(f"Я собираюсь стереть фаил {filename}.")
print("Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C).")
print("Если хотите стереть нажмите клавишу Enter.")
input('?')
print('Открытие файла')

target = open("filename", 'w')

print('Очистка файла. До свидания!')

target.truncate()

print('Теперь я запрашиваю у вас строки.')

line1 = input('строка 1: ')
line2 = input("строка 2: ")
line3 = input("строка 3: ")
print('Теперь я запишу в фаил.')

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print('И наконец закрою фаил.')

target.close()