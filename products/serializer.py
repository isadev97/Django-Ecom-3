from rest_framework import serializers 
from products.models import Product
from tags.serializer import ReadTagMinSerializer, ReadTagSerializer

class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'description', 'tags', 'price', 'quantity', 'image',)


class ReadProductSerializer(serializers.ModelSerializer):
    
    tags = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_tags(self, product):
        product_tags = product.tags.all().only('id', 'name', 'slug')
        return ReadTagMinSerializer(instance=product_tags, many=True).data
        # product_tags = product.tags.all()
        # return ReadTagSerializer(instance=product_tags, many=True).data
        