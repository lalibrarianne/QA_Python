import random
i = 0
a = int(input('введите начало диапазона: '))
b = int(input('введите конец диапазона: '))
for i in range(a, b):
    i = random.randint(a, b)
print(i)
    
import random
cube = random.randint(1, 6)
print(f'вы выбросили', cube)