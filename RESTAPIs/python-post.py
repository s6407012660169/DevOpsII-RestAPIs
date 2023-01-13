import requests
api_url = 'https://jsonplaceholder.typicode.com/todos'
#api_url = 'https://api.github.com/users/sachini950412'

todo = {
    "userId": 909,
    "id": 909,
    "title": 'Sachini Merangika',
    "complete": False
}

response = requests.post(api_url,json =todo)

print(response.json())
print(response.status_code)