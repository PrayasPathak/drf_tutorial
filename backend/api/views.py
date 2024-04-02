from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data)
