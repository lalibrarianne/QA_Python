a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
def divide(a, b):
    return a/b
try:
    print(divide(a,b))
except ZeroDivisionError:
    print('Ошибка')

try:
    with open(r'C:\Users\ATTEKPC\Desktop\Doc.txt', 'r', encoding = "utf-8" ) as file:
        d = file.read()
    print(d) 
except FileNotFoundError:
    print('Ошибка')