import requests
api_url = 'https://jsonplaceholder.typicode.com/todos/1'
#api_url = 'https://api.github.com/users/sachini950412'
response = requests.get(api_url)

print(response.json())

todo = {
    "userId": 1,
    "id": 1,
    "title": 'Sachini Merangika',
    "complete": True
}

response = requests.put(api_url, json=todo)

print(response.json())
print(response.status_code)