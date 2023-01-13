import requests
api_url = 'https://jsonplaceholder.typicode.com/todos/1'
#api_url = 'https://api.github.com/users/sachini950412'

response = requests.get(api_url)

print(response.json())
print(response.status_code)