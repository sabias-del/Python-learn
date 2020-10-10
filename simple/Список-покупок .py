# Это мой список покупок

shoplist = ['яблоки', 'бублик', 'морковь', 'свеклу', "бананы"]
print("я должен сделать", len(shoplist), "покупки.")

print("Покупки:", end="")
for item in shoplist:
    print(item, "", end="")

print('\nТакже нужно купить риса.')
shoplist.append("рис")
print("Теперь список товаров таков:", shoplist)

print("Отрисую-ка я свой список")
shoplist.sort()
print("Отрисованый список покупок выглядит так:", shoplist)

print("Первое что нужно купить, это: ", shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print("Теперь мой список:", shoplist)
