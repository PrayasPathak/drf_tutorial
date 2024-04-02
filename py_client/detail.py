import requests
from pprint import pprint

# Get a product detail
endpoint = "http://localhost:5000/api/products/2"
product_detail = requests.get(endpoint)
pprint(product_detail.json())
