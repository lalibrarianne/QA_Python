import random 
money = 150
prime = random.randint(1, money)

def calc(km, money, prime):
    return multiply (km, money)
while True:
    km = input('Введите расстояние в км:')
    if km == 0:
        print(prime)   
    else:
        print(km*money)
    