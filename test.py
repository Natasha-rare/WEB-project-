from requests import post, get

print(get('http://localhost:5000/api/v1/users').json())