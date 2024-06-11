import re

def validate_text_length():
    try:
        with open (r'C:\Users\ATTEKPC\Desktop\Ddoc.txt', 'r', encoding = 'utf-8') as file:
            a = str(file.read())
            b = re.sub(r'[^\w\s]','', a)
            words = b.split()
            print(len(words))
        
            if len(words) > 100:
                return False
            else:
                return True
            
    except FileNotFoundError:
        return 'файл не найден'
print(validate_text_length())
