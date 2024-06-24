import requests
api_key = 'mLy8w6gPChVVTgsQVDQW5DE5cMCb1JBdpahuawG4'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
response = requests.get(url)
   
if response.status_code == 200:
    data = response.json()
    image_url = data.get('hdurl')
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open('nasa.jpg', 'wb') as file:
            file.write(image_response.content)
        print('успех')
    else:
        print('косяк')
    print(f'title: {data.get('title')}')
    print(f"explanation: {data.get('explanation')}")
    print(f"hdurl: {data.get('hdurl')}")
    print(f"url: {url}")
else:
    print('fail')
