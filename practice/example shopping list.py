products = ['яблоки','груши','веники','угли','мясо']
prices = [100,200,300,400,500]
basket = sum(prices)
if basket >= 800:
    print(basket*0.9)
elif basket == 1500:
    print(basket*0.7)