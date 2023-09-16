from products.views import CreateProductView, ListProductView
from django.urls import path 

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('list/', ListProductView.as_view(), name='product-list')
]

