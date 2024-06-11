import random

questions = [
    'Сколько будет 2+2?',
    'Какой день недели первый?',
    'Что больше море или океан?',
    ]
answers = [
    '4','понедельник','океан'
]

def viktorina():
    used = []    
    while len(used) != len(questions):
        a = random.choice(questions)
        if a not in used:
            print(a)
            used.append(a)
            mark = 0    
            answer = input('Введите ответ: ')
            if answer in answers:
                mark += 1 
            else: 
                mark -= 1
        else:
            continue
    
    return mark    
    
print(viktorina())