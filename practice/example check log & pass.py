login = input('login: ')
password = input('password: ')

if len(login) >=6 and len(password)>=8:
    has_uper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_uper and has_digit:
        print("Вход выполнен")
    else:
        print("Ошибка должна быть одна заглавная и хотя бы одна цифра")
else:
    print("Ошибка: логин должен быть не менее 6 символов, а пароль не менее 8 символов")       


    p = input('Введите пароль: ')
def check_password(p):
    if any(char.isupper() for char in p):
        return True
    if any(char.isdigit() for char in p):
        return True
    if len(p)>=8: 
        return True
    if p.startswith(char.isupper() for char in p):
        return True
    else:
        return False
print(check_password(p))    