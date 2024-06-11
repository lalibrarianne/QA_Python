import requests 

site = input('Введите адрес сайта: ')

try:
    response = requests.get(site)
    response.raise_for_status()
    status_code = response.status_code
    if status_code == 200:
        print('True')
    else:
        print('False')

except:
    print('ошибка запроса')

