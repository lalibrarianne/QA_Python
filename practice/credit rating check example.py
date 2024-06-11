rating = int(input('rating: '))
income = int(input('income: '))
if rating >= 7:
    print('Ваш кредитный рейтинг хороший')
    if income >= 5000:
        print('Ваш доход выше 5000$')
        print('Вам одобрен кредит')
    else:
        print('Ваш доход ниже 5000$')
        print('Вам не одобрен кредит')
else:
    print('Ваш кредитный рейтинг ниже 7')


