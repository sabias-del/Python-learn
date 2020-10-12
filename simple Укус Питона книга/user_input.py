def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


input = input("Введите text: ")
something = str.upper(input.replace(' ', ''))
print(something)

if (is_palindrome(something)):
    print("Это настоящий палиндром")
else:
    print("Нет, это не палиндром")
