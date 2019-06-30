from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product

# Create your views here.

# all products lis view
class ProductListView(ListView):
    queryset = Product.objects.all().exclude(quantity=0)
    template_name = 'products/products.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 10


# product detail page
class ProductDetailView(DetailView):
    model = Product

    
# product detail page    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product 
    fields = ['name', 'description', 'image', 'price', 'quantity', 'category', 'location']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
# product detail page       
        
class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Product 
    fields = ['name', 'description', 'image', 'price', 'quantity', 'category', 'location']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        return False
        
        
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'
    
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        return False
