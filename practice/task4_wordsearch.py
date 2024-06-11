import random
import re

def search():
    try:
        with open (r'C:\Users\ATTEKPC\Desktop\Doc.txt', 'r', encoding = 'utf-8') as file:
            line = file.readlines()
            found_lines = []            
            search_word = 'мех'


            for search_word in line:
                b = line.count(search_word) 
                return b   

            for search_word in line:
                if line in file:
                    found_lines.append(line)
                    return found_lines
                
   
    except FileNotFoundError:
        return 'файл не найден'
    
    
    
print(search())