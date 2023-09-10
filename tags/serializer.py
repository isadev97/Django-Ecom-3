from rest_framework import serializers
from tags.models import Tags

# types of serializer by name 
# read serializer is used read operation of database
# write serializer is used to write operation of database

class WriteTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'slug')

class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'slug', 'created_at', 'updated_at')

