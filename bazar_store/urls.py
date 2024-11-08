from django.urls import path
from bazar.views import ProductSearchView, ProductDetailView, AddSaleView, SaleListView

urlpatterns = [
    path('api/items', ProductSearchView.as_view(), name='product-search'),
    path('api/items/<int:id>', ProductDetailView.as_view(), name='product-detail'),
    path('api/addSale', AddSaleView.as_view(), name='add-sale'),
    path('api/sales', SaleListView.as_view(), name='sale-list'),
]