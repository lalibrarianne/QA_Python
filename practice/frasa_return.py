import random
import re

def frasa():
    try:
        with open (r'C:\Users\ATTEKPC\Desktop\Doc.txt', 'r', encoding = 'utf-8') as file:
            a = str(file.read())
            
            b = re.sub(r'[^\w\s]','', a)
            words = b.split()
        
            length = random.randint(3,7)
            line = ' '.join(random.choice(words) for _ in range(length))
        return line
    except FileNotFoundError:
        return 'файл не найден'
print(frasa())

