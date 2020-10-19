# Импорт модуля Sys его библиотеки argv
from sys import argv
# команда которой присваиваем имя для библиотеки argv
script, filename = argv
# Новая переменная txt с указанным именем который передали в командную строку
txt = open(filename)
# Печать содержимого filename
print(f'Содержание файла {filename}:')
# Чтение файла без условия
print(txt.read)

print('Снова введите имя файла:')
file_again = input('> ')
txt_again = open(file_again)
print(txt_again.read())
