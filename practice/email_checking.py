
def check_emails(email):


    #проверка на наличие собаки
    if '@' not in email:
        return False
    #делим адрес по символу собаки
    parts = email.split('@')


    #проверку н наличие логина и домена
    if len(parts) != 2:
        return False
   
    login,domain = parts[0],parts[1]
    #проверка формата логина
    if not login or not login.replace('.','').isalnum():
        return False
    elif len(login) < 6:
        return False
   
    #проверка формы домена
    domain_par = domain.split('.')
    if len(domain_par) <2 or any(not part.isalnum() for part in domain_par):
        return False
    return True


print(check_emails('example@email.com')) # True
print(check_emails('invalid.email@domain'))  #False
print(check_emails('another.example@sub.domain.com'))  #True
print(check_emails('invalid_enother?@domain.name')) # false
print(check_emails('we@domain.name')) # false

