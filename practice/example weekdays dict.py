days = {
    "пн":"Понедельник",
    "вт":"Вторник",
    "ср":"Среда",
    "чт":"четверг",
    "пт":"Пятница",
    "сб":"суббота",
    "вс":"воскресенье",
}
day = input()
if day in days:
    type_day = "будний" if day in ['пн','вт','ср','чт','пт'] else 'выходной'
    print(f'сегодня {days[day]}, {type_day} день')
else:
    print("неверный тип даты")