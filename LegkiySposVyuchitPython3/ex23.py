import sys #module system
# оболочка командной строки (срипт), кодировка(utf=), Ошибки в виде сообщений
script, encoding, error = sys.argv
# функция мейн(фаил, кодировка, ошибки)
def main(language_file, encoding, errors):
    # линия = фаил.чтениефайла
    line = language_file.readline()
# если линия:
    # печать линии(линия, кодировка(utf=), ошибки)
    # возврат main(языковый_фаил, кодировка(utf=), ошибки)
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# функция печати линии(линия, кодировка(), ошибки)
    # следующий язык = линия.выборка
    # кодируем следующий язык(слово) в код
    # разкодируем следующий язык(слово) в декод
    # печать для наглядного понимания
def print_line(line, encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    coked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, '<===>', coked_string)

#Фаил с язками открыть кодировка такая вот
#Функция main (языки, кодировка, ошибки)
languages = open('languages.txt', encoding='utf-8')
main(languages, encoding, error)