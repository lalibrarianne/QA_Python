b = 12

counter = 5 
while counter > 0:
    a = int(input('Введите число: '))
    if a < b:
        print('Ваше число меньше')
    elif a > b:
        print('Ваше число больше')
    elif a == b:
        print('Вы выиграли')
        break
    counter -= 1
print('стоп игра')
