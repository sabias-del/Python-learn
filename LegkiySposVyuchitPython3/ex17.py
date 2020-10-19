from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f'Копирование данных из файла {from_file} to {to_file}')

# Можете следующие  две строки разместить в одну?

in_file = open(from_file)
indata = in_file.read()

print(f'Исходный размер файла {len(indata)} байт')
print('Готов, нажмите клавишу Enter для продолжения или CTRL+C для отмены.')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Отлично" )

out_file.close()
in_file.close()