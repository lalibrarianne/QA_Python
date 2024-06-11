a = [78, 25, 15, 118, -200, 800, -1]
for i in a:
    if i < 0:
        print("отрицательное")
        break
    print(i)

copies = 0
maximum = 10
i = 1
while i > copies:
    if i <= maximum:
        found = True
        print(i, 'pass')
    i+=1
else:
    print('fail')