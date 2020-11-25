then_things= "яблоки апельсин вороны телефоны свет сахар"
print("Погодите,  тут меньше 10 объектов.  Давайте исправим это.")
stuff = then_things.split(" ")
more_stuff = ["День",  "Ночь",  "Песня",  "Мишка", "Кукуруза",  "Банан",  "Девочка",  "Мальчик"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Добовляем: ", next_one)
    stuff.append(next_one)
    print(f"Теперь у нас {len(stuff)} обьектов.")

print("Итак:  ",  stuff)

print("Давайте сделаем что то с нашими обьектами.")

print(stuff[1])

print(stuff[-1]) # хм интересно

print(stuff.pop())

print(" ".join(stuff)) # что круто

print('#'.join(stuff[3:5])) # просто супер !

