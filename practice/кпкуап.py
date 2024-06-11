p = input('Введите пароль: ')
def add(p):
    return len(p)
if len(p)>=8:
    has_uper = any(char.isupper() for char in p)
    has_digit = any(char.isdigit() for char in p)
if has_uper and has_digit:
    print('принято')
else:
    print('ошибка')