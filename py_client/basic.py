import requests

# endpoints = "https://httpbin.org/"
endpoints = "https://httpbin.org/anything"

get_response = requests.get(endpoints, json={"page": "anything"})
print(get_response)
# print(get_response.text)
print(get_response.json())
print(get_response.status_code)
