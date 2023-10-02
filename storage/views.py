"""
This file is used to define the views for the storage app.
"""

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView, ListView, DeleteView
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
    context_object_name = 'products'


class DeleteProductView(LoginRequiredMixin, DeleteView):
    """Delete Product View"""
    success_url = reverse_lazy('list_products')
    model = Product
    template_name = 'storage/delete_product.html'

class CreateProductView(LoginRequiredMixin, FormView):
    """
        Create Product View
    """
    template_name = 'storage/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_products')

    def get_form_kwargs(self):
        """
            This method is used to add extra arguments to the form.
        """
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """
            This method is used to validate the form.
        """
        self.object = form.save()
        return super().form_valid(form)


class EditProductView(LoginRequiredMixin, UpdateView):
    """
        Edit Product View
    """
    model = Product
    template_name = 'storage/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_products')

    def get_form_kwargs(self):
        """
            This method is used to add extra arguments to the form.
        """
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """
            This method is used to validate the form.
        """
        self.object = form.save()
        return super().form_valid(form)

class ListTransactionView(LoginRequiredMixin,ListView):
    """
        List Transaction View
    """
    model = Transaction
    template_name = 'storage/list_transactions.html'
    context_object_name = 'transactions'
