from django.urls import path
from .views import CartItemListView, CartDetailView

urlpatterns = [
    path('cart/', CartItemListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
]
