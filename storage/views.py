"""
This file is used to define the views for the storage app.
"""

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, ListView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
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
    http_method_names = ['get', 'post']

    def form_valid(self, form):
        """
            This method is used to delete the product.
        """
        instance = self.get_object()
        description = f'{self.request.user.username} Deleted - {instance.name}'
        Transaction.objects.create(
            user=self.request.user,
            product_name=instance.name,
            transaction_type=2,
            description=description
        )
        return super().form_valid(form)

class CreateProductView(LoginRequiredMixin, FormView):
    """
        Create Product View
    """
    template_name = 'storage/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_products')

    def form_valid(self, form):
        """
            This method is used to validate the form.
        """
        data = form.cleaned_data
        stock = Stock.objects.create(
            quantity=data['quantity']
        )
        product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            image=data['image'],
            stock=stock
        )
        description = f'{self.request.user.username} Created - {product.name}'
        Transaction.objects.create(
            user=self.request.user,
            product_name=product.name,
            transaction_type=0,
            description=description
        )
        return super().form_valid(form)

class EditProductView(LoginRequiredMixin, FormView):
    """
        Edit Product View
    """
    template_name = 'storage/edit_product.html'
    success_url = reverse_lazy('list_products')
    form_class = ProductForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_instance = None
        self.stock_instance = None

    def get_initial(self):
        """
            This method is used to add initial data to the form.
        """
        self.product_instance = get_object_or_404(Product, id=self.kwargs['pk'])
        self.stock_instance = self.product_instance.stock
        return {
            'name': self.product_instance.name,
            'description': self.product_instance.description,
            'quantity': self.stock_instance.quantity,
            'image': self.product_instance.image
        }


    def form_valid(self, form):
        """
            This method is used to validate the form.
        """
        # Update product
        data = form.cleaned_data

        self.product_instance.name = data.get('name', self.product_instance.name)
        self.product_instance.description = data.get('description', self.product_instance.description)
        self.product_instance.image = data.get('image', self.product_instance.image)
        self.product_instance.save()
        # Update self.stock_instance

        self.stock_instance.quantity = data.get('quantity', self.stock_instance.quantity)
        self.stock_instance.save()
        # Create transaction
        description = f' {self.request.user} Edited - {self.product_instance.name}'
        Transaction.objects.create(
            user=self.request.user,
            product_name=self.product_instance.name,
            transaction_type=1,
            description=description
        )
        return super().form_valid(form)



class ListTransactionView(LoginRequiredMixin,ListView):
    """
        List Transaction View
    """
    model = Transaction
    template_name = 'storage/list_transactions.html'
    context_object_name = 'transactions'
