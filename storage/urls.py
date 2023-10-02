"""
    Urls for storage app
"""

# Django
from django.urls import path

# Views
from storage.views import (
    ProductDetailView,
    ListProductsView,
    CreateProductView,
    DeleteProductView,
    EditProductView,
    ListTransactionView
)

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('', ListProductsView.as_view(), name='list_products'),
    path('create/', EditProductView.as_view(), name='create_product'),
    path('<int:pk>/edit/', CreateProductView.as_view(), name='edit_product'),
    path('<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
    path('transactions/', ListTransactionView.as_view(), name='list_transactions'),
]
