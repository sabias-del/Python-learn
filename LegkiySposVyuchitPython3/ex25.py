

def break_words(stuff):
    '''Эта функция разбирает текст на слова.'''
    words = stuff.split(" ")
    return words

def sort_words(words):
    '''Сортируем слова'''
    return sorted(words)

def print_fist_word(words):
    '''Выводим первое слово после извлечения.'''
    word = words.pop(0)
    print(word)

def print_last_word(words):
    '''Выводим последние слово после извлечения.'''
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    '''Принимаем целое предложение и сортируем слова.'''
    words = break_words(sentence)
    return sort_words(words)

def print_fist_and_last(sentence):
    '''Выводит первое и последние слова предложения.'''
    words = break_words(sentence)
    print_fist_word(words)
    print_last_word(words)

def print_fist_and_last_sorted(sentence):
    '''Сортируем слова, затем выводим первое и последние.'''
    words = sort_sentence(sentence)
    print_fist_word(words)
    print_last_word(words)
    