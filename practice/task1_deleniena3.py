def tri():
    list = [1, 2, 3, 4, 44, 52, 45, 12, 33]
        
    spisok = []
    
    for i in list:
        if i % 3 == 0:
            spisok.append(i)
            continue
       
    return spisok

print(tri()) 



