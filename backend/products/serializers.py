from rest_framework import serializers
from .models import Product
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    related_products = ProductInlineSerializer(
        source="user.product_set.all", many=True, read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "user",
            "url",
            "id",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
            "related_products",
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
