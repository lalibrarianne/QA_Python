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

for name, hours in skud.items():
print(f'{name}: {hours}')

