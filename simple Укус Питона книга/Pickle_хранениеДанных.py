import pickle

# имя файла с покупками который мы сохраняли или любой лист
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ["яблоко", "манго", "морковь"]
# запись в файл
a = open(shoplistfile, "wb")
pickle.dump(shoplist, a)  # помещаем обьект в фаил

a.close()

del shoplist  # уничтожаем переменную shoplist

# Чтение из хранилища

a = open(shoplistfile, 'rb')
storedlist = pickle.load(a)  # загружаем обьект из файла

print(storedlist)
