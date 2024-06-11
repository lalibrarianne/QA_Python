import random
my_list = []
count = 10
while count > 0:
    a = random.randint(1, 1000)
    my_list.append(a)
    count -= 1
def add(my_list):
    return sum(my_list)
res_1 = add(my_list)
print('Сгенерированный список:', my_list)
print('Сумма элементов:', res_1)
b = int(input('Введите число: '))
def divide(res_1, b):
    return res_1/b
try:
    print('Результат деления:', divide(res_1, b))
except ZeroDivisionError:
    print('Ошибка')



    import statistics
a = [6,7,9,6,10]
def mark(a):
    return statistics.mean(a)
print(mark(a))


d = [6,7,9,6,10]
def srednee(marks):
    return sum(marks) / len(marks)

print(srednee(d))

operator = input('operator:')
num1 = input('num1:')
num2 = input('num2:')
