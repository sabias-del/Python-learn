

import random
from urllib.request import urlopen
import sys


Word_Url="http://learncodethehardway.org/words.txt"
words = []

PHRASES = {
    "class %%%(%%%):":
    "Создается класс с именем %%%, наследующим %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
    "Класс %%% комбинирует __init__ с параметрами self и параметрами ***.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "Класс %%% комбинирует функцию с именем *** с параметрами ***.",
    "*** = %%%()":
    "Создается *** как экземляр класса %%%.",
    "***.***(@@@)":
    " Из *** получается функция ***, а затем вызывается с параметром self , @@@.",
    "***.*** = '***'":
    " Из *** получается атрибут ***, а затем устанавливается равным '***'."
}

# Тренировка запоминания фраз

if len(sys.argv) == 2 and sys.argv[1] == 'russian':
    PHRASES_FIST = True
else:
    PHRASES_FIST = False

# Подгружаем слова с сервера

for word in urlopen(Word_Url).readlines():
    words.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_name = [w.capitalize() for w in
                   random.sample(words, snippet.count('%%%'))]
    other_names = random.sample(words, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count('@@@')):
        param_count = random.randint(1,3)
        param_names.append(", ".join(random.sample(words, param_count)))

    for sentence in snippet, phrase:
        results = sentence[:]

        # вымешленные имена классов

        for word in class_name:

            results = results.replace('%%%', word, 1)

        # вымешленные другие имена

        for word in other_names:
            results = results.replace('***', word, 1)

        # список вымешленных параметров

        for word in param_names:
            results = results.replace('@@@', word, 1)
        
        results.append(results)
    return results

# выполнение пока не нажаты сочетания клавиш CTRL+Z

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIST:
                question, answer = answer, question

            print(question)

            input(">")
            print(f"ОТВЕТ: {answer}\n\n")
except EOFError:
    print("\nПока")