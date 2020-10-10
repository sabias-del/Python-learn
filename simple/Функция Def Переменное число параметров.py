def total(a=5, *numbers, **phonebook):
    print("a", a)

    for single_item in numbers:
        print("singel_item", single_item)
    for fist_part, second_part in phonebook.items():
        print(fist_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
