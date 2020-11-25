import requests
import json
import csv
import random
from time import sleep
from bs4 import BeautifulSoup as BS

# headers from браузер агент чтобы нас видели как клиента браузера а не как бота антибан 1.0
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
}
# #
# #
# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
# req = запрос получить (сайт, хедер(антибан))
# req = requests.get(url, headers=headers)
# полученный результат в текст
# src = req.text
# #print(src)
# для открытого документа "W" как фаил
# with open('index.html', 'w') as file:
# фаил вписать в (переменная)
#     file.write(src)
#
# для открытого документа как фаил
# with open('index.html') as file:
# переменная равна фаил чтение
#     src = file.read()
# BS переменная кодировка парсера
# soup = BS(src, 'lxml')
# все сылки на href = BS найти все класс Href
# all_product_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
# создание пустого словоря переменной
# all_product_dict = {}
# для итем в переменной сылок
# for item in all_product_hrefs:
      #переменная текст
#     item_tex = item.text
      #переменная сылочка + сайт
#     item_href = 'https://health-diet.ru' + item.get('href')
      # добавим в словарь итем текст = итем сылочка
#     all_product_dict[item_tex] = item_href
#     #print(f"{item_tex} : {item_href}")
# для открытого переменная в виде джион вписываем в фаил
# with open('all_product_dict.json', 'w') as file:
# json dunmp переменный словарь фаил форматирование=4 русский шрифт = фелсе
#     json.dump(all_product_dict, file, indent=4, ensure_ascii=False)

# для открытого переменная json как фаил
with open("all_product_dict.json") as file:
    # все категории = json загрузка (фаил)
    all_categories = json.load(file)
# итарация подсчет = цифра(протяженность(всекатегории)) - 1
iteration_count = int(len(all_categories)) - 1
# счет
count = 0
# печать все итерации (количество итераций)
print(f"Всего итераций: {iteration_count}")
# для категорий имени категорий сылок в все категории
for category_name, category_href in all_categories.items():
    # переменная из которой будут удалены символы словаря
    rep = [",", " ", "-", "'"]
    for item in rep:
        # для итем в rep
        # если итем в категории имени то
        if item in category_name:
            # категории имени  = категории имени заменить ( что , на_что)
            category_name = category_name.replace(item, "_")
    # req = request получить(сайт = сылки , антибот хедер)
    req = requests.get(url=category_href, headers=headers)
    # результат  = req как текст
    src = req.text
    # с открытым(где папка дата / подсчет / имя категории как html, 'w' вписать ) как фаил:
    with open(f"data/{count}_{category_name}.html", "w") as file:
        # фаил писать(src)
        file.write(src)
    # с открытым(где папка дата / подсчет / имя категории как html ) как фаил:
    with open(f"data/{count}_{category_name}.html") as file:
        # src = file чтение
        src = file.read()
    # soup  = BS(фаил, парсер)
    soup = BS(src, "lxml")

    # проверка страницы на наличие таблицы с продуктами
    alert_block = soup.find(class_="uk-alert-danger")
    # если алертблок не пуст то продолжаем
    if alert_block is not None:
        continue

    # собираем заголовки таблицы (из класса "mzr-tc-group-table" )
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    # с открытым(где папка дата / подсчет / имя категории как CSV 'вписать', кодировка UTF-8 ) как фаил:
    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        # writer  = CVS writer (фаил)
        writer = csv.writer(file)
        # writer метод врайтроу как выглядит список внтури для прощего
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )

    # собираем данные продуктов
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
    # создаем кортеж инфо
    product_info = []
    # для итем в продукт дате:
    for item in products_data:
        # продукт  =  итем найти все td
        product_tds = item.find_all("td")

        title = product_tds[0].find("a").text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        # продукт инфо добавить опять таки список как мы видим имя и значение
        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )
        # с открытым(где папка дата / подсчет / имя категории CVS , A - добавить, кодировка такая то ) как фаил:
        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:

            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
    # с открытым(где папка дата / подсчет / имя категории как json , a добавить, кодировка ) как фаил:
    with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        # json dump( продукт инфо, file, табуляция, языковая проверка нет)
        json.dump(product_info, file, indent=4, ensure_ascii=False)
    # после всего кода выше +1 к счету
    count += 1
    # выводим счет категорию имени - записан
    print(f"# Итерация {count}. {category_name} записан...")
    # подсчет итераций = итарация - 1
    iteration_count = iteration_count - 1
    # если итерация равна 0
    if iteration_count == 0:
        # печать работа завершена
        print("Работа завершена")
        # остановка
        break
    # печать количество итераций
    print(f"Осталось итераций: {iteration_count}")
    # сон случайно ранд рендж от 2 до 4 секунд
    sleep(random.randrange(2, 4))