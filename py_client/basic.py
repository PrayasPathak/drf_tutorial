import requests

# endpoints = "https://httpbin.org/"
# endpoints = "https://httpbin.org/anything"
endpoints = "http://localhost:5000/api/"
get_response = requests.get(
    endpoints, params={"title": "django rest framework"}, json={"page": "anything"}
)
# print(get_response.text)
print(get_response.json())
# print(get_response.json()["message"])
print(get_response.status_code)
