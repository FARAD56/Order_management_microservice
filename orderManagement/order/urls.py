# urls.py

from django.urls import path
from .views import OrderCreateView, OrderDetailView, UserOrdersView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    path('orders/create', OrderCreateView.as_view(), name='order-create'),
    path('users/<int:userId>/orders', UserOrdersView.as_view(), name='user-orders'),
    path('orders/update/<int:pk>', OrderUpdateView.as_view(), name='order-update'),
    path('orders/delete/<int:pk>', OrderDeleteView.as_view(), name='order-delete'),
]
