from rest_framework import serializers 
from products.models import Product

class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'description', 'tags', 'price', 'quantity', 'image',)