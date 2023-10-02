"""
    Urls for storage app
"""

# Django
from django.urls import path

# Views
from storage.views import ProductDetailView, ListProductsView, CreateProduct

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', ListProductsView.as_view(), name='list_products'),
    path('create/', CreateProduct.as_view(), name='create_product'),
    path('update/<int:pk>/', CreateProduct.as_view(), name='update_product'),
    path('delete/<int:pk>/', CreateProduct.as_view(), name='delete_product'),
    path('transactions/', CreateProduct.as_view(), name='list_transactions'),
]
