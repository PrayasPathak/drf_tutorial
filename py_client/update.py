import requests
from pprint import pprint

# Get a product detail
endpoint = "http://localhost:5000/api/products/2/update/"
data = {"title": "Face wash", "price": 80.00, "content": "An amazing product"}

product_detail = requests.put(endpoint, json=data)
pprint(product_detail.json())
