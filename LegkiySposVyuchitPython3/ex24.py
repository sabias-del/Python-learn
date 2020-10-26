print("Давайте попрактикуемся!")
print('Вы должны знать об управляющих последовательностях с символом \\, которые:')
print('\n управляет переносом строк и \t отступами.')

poem='''
\tДля счастья
мне совсем много не надо.
Хочу тебя\n
я нежно обнимать.
Хочу всегда
я быть с тобою рядом
\n\tникогда не отступать !
'''
print("-----------------------------")
print(poem)
print("-----------------------------")

five=10-2+3-6
print(f'Здесь должна быть {five}')

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

beans, jars, crates = secret_formula(start_point)


# помните, что это еще один способ форматирования строки
print("Начиная с: {}".format(start_point))
# так же как со строкой f''
print(f'У нас есть {beans} бобов, {jars} банок и {crates} ящиков.')
start_point = start_point / 10

print("Mbi также можем сделать это таким образом:")
formula = secret_formula(start_point)
# просто способ применить список к формуле строке
print('У нас есть {} бобовб, {} банок и {} ящиков.'.format(*formula))