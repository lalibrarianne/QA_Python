a = input('марка: ')
b = int(input('год выпуска: '))
c = int(input('пробег: '))
d = input('состояние: ')

foreign = ['mercedes', 'bmw', 'cherry','toyota', 'kia'],
russian = ['волга', 'москвич'],

for a in foreign:
    if b >= 2020 and c == 0 and d == 'новый':
        print('price 1M')
        if d == 'б/у' and c <= 100000 and b < 2020 or b > 2000:
            print('price 0.5M')
        if c > 100000:
            print('price 0.2M')
    else:
        print('price 20000'),
for a in russian:
    print('price 20000')
