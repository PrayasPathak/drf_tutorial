import requests
from pprint import pprint

# List products
products_list_endpoint = "http://localhost:5000/api/products/"
products_list = requests.get(products_list_endpoint)
pprint(products_list.json())
