poem = '''\
Программировать весело. 
Если работа скучна,
Чтобы придать ей весёлый тон - 
используй Python!'''

f = open('poem.txt', "w")  # открываем фаил для записи
f.write(poem)  # записываем файлы в текст
f.close()

f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:  # нулевая длина файла что означает что текст прочтеться до конца
        break
    print(line, end="")

f.close()
