import re
text = input('Скопируйте сторку из текста: ')
a = re.sub(r'[^\w\s]', '', text)
word = word.strip(', .'.lower())
my_dict = {i:word.count(i) for i in set(word)}
def count_letters(a):
    return my_dict
print(len(a))
print(count_letters(a))

uniq_words = {}
words_count = {}

for word in words:
    word = word.strip(', .'.lower())
    if word in uniq_words:
        index = uniq_words.index(word)
        words_count[index] += 1
    else:
        uniq_words.append(word)
        words_count.append(1)
