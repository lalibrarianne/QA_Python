import random
import re

def word_frequency():
    try:
        with open (r'C:\Users\ATTEKPC\Desktop\Doc.txt', 'r', encoding = 'utf-8') as file:
            a = str(file.read())
            
            b = re.sub(r'[^\w\s]','', a)
            words = b.split()
            print(words)

            uniq_word = 0
            word_count = 0
            my_dict = {}
            if words in uniq_word:
                index = uniq_word.index(words)
                word_count[index] += 1
            else:
                my_dict[uniq_word] = word_count
        return my_dict
    except FileNotFoundError:
        return 'файл не найден'
print(word_frequency())