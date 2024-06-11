import random

def sumarising():
    num = random.randint(10, 1000)
    sum_of_digits = 0
    num_str = str(num)
    print(num)
    
    for a in num_str:
        sum_of_digits += int(a)
        
    return sum_of_digits

print(sumarising())


