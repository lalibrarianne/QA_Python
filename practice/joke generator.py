import random

joke_template = [
    'Почему {} катится вниз?',
    'Потому что {} смеятся над ним!',
    'Кто {} в книгах?',
    'Кто {}?',
    'Что сказал {} ему {} когда они встретились ?'
]
joke_elements = [
    'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
    'водитель','улитка'
]

def generator():
    try:
        for i in joke_template:
            i = str(random.choice(joke_template))
        for j in joke_elements:
             j = random.choice(joke_elements)
        fun = i.format(j)
    except IndexError:
        l = random.choice(joke_elements)
        l != j
        fun = i.format(j, l)
    return fun
print(generator())