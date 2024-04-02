import requests
from pprint import pprint

# Get a product detail
product_id = input("Enter the product id you want to delete? ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not a valid id")
if product_id:
    endpoint = f"http://localhost:5000/api/products/{product_id}/delete/"
    product_detail = requests.delete(endpoint)
    pprint(product_detail.status_code)
