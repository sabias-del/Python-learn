def get_error_details():
    return (2, "описание ошибки 2")


errnum, errstr = get_error_details()
print(errstr)
print(errnum)

# Чтобы интерпретировать результат как «(a, <всё остальное>)»,
# нужно просто поста-вить звёздочку, как это делалось для параметров функций :

a, *b = [1, 2, 3, 4]

print(a)
print(b)

# Блоки в одно выражение
flag = True
if flag: print('DA')
