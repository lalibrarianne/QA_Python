my_dict = {}
my_dict ['в'] = 1
my_dict ['а'] = 1
my_dict ['л'] = 1
my_dict ['е'] = 1
my_dict ['н'] = 1
my_dict ['о'] = 1
my_dict ['к'] = 1

print("валенок")
for i, q in my_dict.items():
    if q>0:
        print(f'{i} : {q}')
    else:
        print(f'{i} : {q}')



word = input('введите слово: ')
new_dict = {}

for i in word:
    if i in new_dict:
        new_dict[i]+=1
    else:
        new_dict[i]=1
print(new_dict)
