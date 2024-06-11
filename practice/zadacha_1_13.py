import random
my_list = []
count = 5
while count > 0:
    a = input('введите слово: ')
    my_list.append(a)
    count -= 1
    
random.shuffle(my_list)
  
print(my_list)
    
