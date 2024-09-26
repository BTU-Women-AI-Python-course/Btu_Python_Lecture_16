from django.urls import path

from product.api_views import ProductView
from product.views import product_list, product_detail, product_create, product_update, product_partial_update, \
    product_delete

urlpatterns = [
    # Function-based views
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('create/', product_create, name='product_create'),
    path('update/<int:pk>/', product_update, name='product_update'),
    path('partial_update/<int:pk>/', product_partial_update, name='product_partial_update'),
    path('delete/<int:pk>', product_delete, name='product_delete'),

    # Class-based views
    path('class_products/', ProductView.as_view(), name='class_product_list'),
    path('class_products/<int:pk>/', ProductView.as_view(), name='class_product_detail')
]
