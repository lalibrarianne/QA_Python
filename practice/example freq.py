text = """""
There are many variants , but most of them do not always have acceptable modifications, for example, humorous inserts or words that do not even remotely resemble Latin. If you need Lorem Ipsum for a serious project, you probably don't want some joke hidden in the middle of a paragraph. Also, all other well-known Lorem Ipsum generators use the same text, which they simply repeat until they reach the desired volume.
"""""
words = text.split()

uniq_words = []
words_count = []

for word in words:
    word = word.strip(',.').lower()

    if word in uniq_words:
        index = uniq_words.index(word)
        words_count[index] += 1
    
    else:
        uniq_words.append(word)
        words_count.append(1)

max_count = max(words_count)
most_common_word = uniq_words[words_count.index(max_count)]

print(f'Наиболее часто встречающеся слово: {most_common_word} встречается {max_count} раз')
