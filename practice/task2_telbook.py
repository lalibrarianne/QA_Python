import re
user_database = {
    "tel1": {'name':'User', 'tel': '+79002301236'},
    "tel2": {'name':'Vasya', 'tel': '+79003625459'},
    "tel3": {'name':'Petya', 'tel': '+79562301478'},
    "tel4": {'name':'Sereja', 'tel': '+79812365476'},
}

def check():
    while True:
        contact = input('tel#')
        if contact == 'base':
            print(user_database)
        name = input('Имя пользователя: ')
        tel = input('Телефон: ')
                                
        if contact in user_database:
            print("есть в базе")
            break
        elif contact not in user_database:   
            if not re.match(r'^\+\d{11}$', tel):
             print('Вы ввели недопустимые значения в адресе почты')
             
            if not re.match(r'^[a-zA-Z-]{2,}$', name):
                print('Вы ввели недопустимые значения в имени')
        print('Зарегистрирован')
        
    return True   
    
check()