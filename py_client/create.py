import requests
from pprint import pprint

# Create a product
product_create_endpoint = "http://localhost:5000/api/products/"
data = {"title": "Guitar", "price": 800.00, "content": "Nice electric guitar"}

product = requests.post(product_create_endpoint, json=data)
pprint(product.json())
