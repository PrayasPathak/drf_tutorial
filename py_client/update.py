import requests
from pprint import pprint

# Get a product detail
endpoint = "http://localhost:5000/api/products/2/update/"
data = {"title": "Face wash", "price": 49.99}

product_detail = requests.put(endpoint, json=data)
pprint(product_detail.json())
