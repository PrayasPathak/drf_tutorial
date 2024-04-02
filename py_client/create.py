import requests
from pprint import pprint

# Create a product
product_create_endpoint = "http://localhost:5000/api/products/"
data = {"title": "Battery", "price": 12.00, "content": "laptop battery"}

product = requests.post(product_create_endpoint, json=data)
pprint(product)
