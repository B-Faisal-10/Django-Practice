import requests


#endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/

get_response = requests.post(endpoint, json={"title": "abc123", "content": "Hello World", "price": "abc123"})

# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())