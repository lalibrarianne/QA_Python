expenses_incomes = {
    'Monday' : {'expenses': 0, 'income':0},
    'Tuesday' : {'expenses': 0, 'income':0},
    'Wednesday' : {'expenses': 0, 'income':0},
    'Thursday' : {'expenses': 0, 'income':0},
    'Friday' : {'expenses': 0, 'income':0},
    'Saturday' : {'expenses': 0, 'income':0},
    'Sunday' : {'expenses': 0, 'income':0}        
}

for day in expenses_incomes:
    expenses = int(input(f'Введите расходы {day}'))
    incomes = int(input(f'Введите доходы {day}'))
    expenses_incomes[day]['expenses'] = expenses
    expenses_incomes[day]['incomes'] = incomes

total_expenses = sum(day['expenses'] for day in expenses_incomes.values())
total_incomes = sum(day['incomes'] for day in expenses_incomes.values())
balance = total_incomes - total_expenses
print('Общий баланс за неделю')
print(f'Расходы: {total_expenses}')
print(f'Доходы: {total_incomes}')
print(f'Баланс: {balance}')