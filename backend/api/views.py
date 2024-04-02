import json
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict


def api_home(request):
    product = Product.objects.all().order_by("?").first()
    data = {}
    if product:
        # data["id"] = product.id
        # data["title"] = product.title
        # data["content"] = product.content
        # data["price"] = product.price
        data = model_to_dict(product, fields=["id", "title", "price"])
    # return HttpResponse(data, headers={"content-type": "application/json"})
    return JsonResponse(data)
