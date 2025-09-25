a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
# Сравнить строки, если совпали, вывести Аааа, не совпали Уууу
if a == b == c:
    print('Оооо')
elif a == b or b == c or a == b:
    print('Аааа')
else:
    print('Уууу')
