my_dict = {}
my_dict ['книги'] = 20
my_dict ['учебники'] = 10
my_dict ['тетради'] = 45
my_dict ['ручки'] = 187

items = tuple(my_dict.items())
print(f'dict', items)


skud = {
    'Сотрудник1' : {'name': 0, 'hours': 0}, 
    'Сотрудник2' : {'name': 0, 'hours': 0},
    'Сотрудник3' : {'name': 0, 'hours': 0} 
}

for employee in skud:
    name = input(f'Введите имя сотрудника: ')
    hours = int(input(f'Введите количество отработанных часов: '))
    skud [employee] ['name'] = name
    skud [employee] ['hours'] = hours
spisok = [(key,value) for key, value in my_dict.items()]
print(spisok)
