with open (r'C:\Users\ATTEKPC\Desktop\text_desk.txt', 'r', encoding="utf-8") as file:
    a = file.read()
print(a)

    line = file.readlines()
    
    for i in range(1, len(line), 2):
        print(line[i])


    i = file.readlines()
    a = 'Редрик'
    for a in i:
        b = i.count(a)
print(b)