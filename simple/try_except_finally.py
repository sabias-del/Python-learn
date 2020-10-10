import time

try:
    f = open('poem.txt')
    while True:  # обычный способ чтения файлов
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла.')
finally:
    f.close()
    print("(Очистка: Закрытие файла)")
