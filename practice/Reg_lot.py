import re
user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}
def check():
    while True:
        email = input('E-mail:')
        name = input('Имя пользователя: ')
        password = input('Пароль: ')
        if email in user_database:
            print("есть в базе")
            break
        elif email not in user_database:   
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z-0-9.-]+\.[a-zA-Z]{2,}$', email):
             print('Вы ввели недопустимые значения в адресе почты')
             
            parts = email.split('@')
            print(parts)
            if len(parts[0])<6:
                print('Не хватает символов в почте')
                
            if not re.match(r'^[a-zA-Z0-9._%+-]{2,}$', password):
                print('Вы ввели недопустимые значения в пароле')
                
            if len(password) < 8:
                print('Не хватает символов в пароле')
                
            if not re.match(r'^[a-zA-Z-]{2,}$', name):
                print('Вы ввели недопустимые значения в имени')
        return True        
            
    
        

check()
print('Зарегистрирован')