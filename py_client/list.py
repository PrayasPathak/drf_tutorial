import requests
from pprint import pprint
from getpass import getpass

# List products

auth_endpoint = "http://localhost:5000/api/auth/"
username = input("Enter username: ")
password = getpass()
auth_response = requests.post(
    auth_endpoint, json={"username": username, "password": password}
)
pprint(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    product_endpoint = "http://localhost:5000/api/products/"
    products_list = requests.get(product_endpoint, headers=headers)
    pprint(products_list.json())
