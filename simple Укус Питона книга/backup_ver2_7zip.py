import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['E:\testbot\simple', 'E:\testbot\simple\today']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'E:\testbot\simple\today'  # Подставьте ваш путь.
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
# today = target_dir
today = target_dir + os.sep + time.strftime('%Y%m%d')
print(today)
# 5. Текущее имя служит именем архива
now = time.strftime("H%M%S")
# 6. Создаем каталог, если его еще нету
if os.path.exists(today):
    os.mkdir('today')  # Создание каталога имя
    print("Каталог успешно создан", today)
else:
    print("Каталог уже есть", today)
# 7. Имя файла
target = now + ".zip"
# 8. Используем команду Zip для помещения файлов в архив
zip_command = "zip -qr {0} {1}".format(target, "".join(source))
# 9. Используем команду запуска
if os.system(zip_command) == 0:
    print("Резервная копия успешно создана", target)
else:
    print("Создание резервной копии НЕ УДАЛОСЬ")
