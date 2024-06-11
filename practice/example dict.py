shop_list = {}

shop_list['яблоки'] = 5
shop_list['Молоко'] = 10
shop_list['баклажан'] = 10

shop_list['хлеб'] = 0

print("список покупок")

for i, q in shop_list.items():
    if q >0:
        print(f'{i}: {q}')
    else:
        print(f'{i}: {q}')


nested_dict = {'key1':{'nested_key1': 'value1'}, 'key2': {'nested_key_2' : 'value2'}}
print(nested_dict['key2']['nested_key_2'])

nested_list = [[1,2],[3,4],[5,6]]
for i in nested_list:
    for j in i:
        print(j)


word = input()
my_dict = {i: word.count(i) for i in set(word)}
print(my_dict)
