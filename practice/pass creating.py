import random
import string
password = []
def generation(password):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = [string.ascii_letters]
    
    b = [',', '#', '^', '&', '*']
    my_list = num+a+b
    c = random.choice(my_list)
    print(my_list)
    print('c=', c)
    count = random.randint(8, 32)
    while count > 0:
        password.append(c)
        count -=1
        

    return password
generation(password)
print(password)

