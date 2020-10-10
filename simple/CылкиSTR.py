name = 'Swaroop'  # Это объект строки

if name.startswith("Swa"):
    print("Да, строка начинается с 'Swa'")
if "a" in name:
    print("Да, она содержит 'а'")

if name.find("war") != -1:
    print("Да, она содержит 'war'")

delimiter = '_*_'
mylist = ['Бразилия', "Россия", "Гватемала"]
print(delimiter.join(mylist))
