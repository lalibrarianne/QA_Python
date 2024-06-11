import re
def tel_check(number):
    try:
        number = input('Введите номер: +')
        if not re.match(r'^[+0-9-]', number):
            return False
        if len(number)<11:
            return False
        else:
            return True
    except ValueError:
        return 'файл не найден'
print(tel_check('+79002301564'))