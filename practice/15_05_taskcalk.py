
def test_calc(operator,num1,num2):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1*num2
        elif operator == '/':
            return num1/num2
        else:
            return 'Ошибочка вышла'
    except ZeroDivisionError:
        return 'не дели на ноль'

     

print(test_calc('+', 5, 3)) 
print(test_calc('-',5,3)) 
print(test_calc('*',5,3)) 
print(test_calc('/',10,0)) 
print(test_calc('?',5,3)) 
