x = int(input())
if x > 0:
    print("x = True")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
elif x == 0:
    print("0")
else:
    print("x is negative")