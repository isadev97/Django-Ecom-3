from products.views import CreateProductView
from django.urls import path 

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='create-product'),
]

