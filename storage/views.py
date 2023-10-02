"""
This file is used to define the views for the storage app.
"""

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView, ListView
from django.urls import reverse_lazy
# Models
from storage.models import Product, Stock, Transaction

# Forms
from storage.forms import ProductForm


User = get_user_model()

class ProductDetailView(LoginRequiredMixin, DetailView):
    """
        Product Detail View
    """
    model = Product
    template_name = 'storage/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        """
            This method is used to add extra context to the view.
        """
        context = super().get_context_data(**kwargs)
        context['stock'] = Stock.objects.get(product=self.object)
        return context


class ListProductsView(LoginRequiredMixin, ListView):
    """
        List Products View
    """
    model = Product
    template_name = 'storage/list_products.html'
    context_object_name = 'product'


class CreateProduct(LoginRequiredMixin, FormView):
    """
        Create Product View
    """
    template_name = 'storage/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('storage:list_products')

    def form_valid(self, form):
        """
            This method is used to validate the form.
        """
        return super().form_valid(form)
