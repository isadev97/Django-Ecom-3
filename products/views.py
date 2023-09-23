from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from products.serializer import WriteProductSerializer, ReadProductSerializer
from django.utils.text import slugify
from rest_framework.generics import ListAPIView
from products.models import Product
from products.filters import SimplePaginationClass
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from products.permissions import MyPermissionClass
from authentication.permissions import IsAuthenticatedAndActiveUser

# Create your views here.
class CreateProductView(APIView):
    
    def post(self, request):
        request_data = request.data 
        request_data.update({'slug' : slugify(request_data.get('name'))})
        serializer = WriteProductSerializer(data=request_data)
        if serializer.is_valid():
            product_instance = serializer.save()
            response_data = ReadProductSerializer(instance=product_instance).data
            return Response(response_data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ReadProductSerializer
    pagination_class = SimplePaginationClass
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    # default ordering
    ordering = ["-id"]
    ordering_fields = ["id", "created_at"]
    search_fields = ['^name']
    filterset_fields = ['price', 'tags', 'quantity']
    # permission_classes = [MyPermissionClass, ]
    # permission_classes = [IsAuthenticatedAndActiveUser, ]
    # To remove classes use empty array 
    # authentication_classes = []
    # permission_classes = []
    # To remove class use None
    # pagination_class = None 
    
    
    def list(self, request, *args, **kwargs):
        print("request user", request.user)
        return super().list(request, *args, **kwargs)