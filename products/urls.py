from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView, 
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    # path('', all_products, name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('post/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
]