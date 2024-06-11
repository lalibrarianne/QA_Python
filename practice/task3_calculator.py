def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return None
    return x/y

def calculator():
    while True:
        a = input('Введите число:')
        b = input('Введите число:')
        
        if not (a.isnumeric() or (a.startswith('-') and a[1:].isnumeric())):
            print('ошибка введи число')
            continue
        if not (b.isnumeric() or (b.startswith('-') and b[1:].isnumeric())):
            print('ошибка введи число')
            continue
       
        a = int(a)
        b = int(b)


        operator = input('Какое действие нужно выполнить (+-/*)? ')


        if operator == "+":
            result = add(a,b)
        elif operator == "-":
            result = subtract(a,b)
        elif operator == "*":
            result = multiply(a,b)
        elif operator == "/":
            result = divide(a,b)
            if result is None:
                print('Ошибка деления на 0')
                continue
        else:
            print("неверная операция")
            continue
        print(result)


calculator()



