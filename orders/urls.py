from django.urls import path
from .views import OrderListCreateView, OrderRetrieveView, ItemListCreateView, ItemRetrieveUpdateDestroyView

urlpatterns = [

    # Pedidos
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveView.as_view(), name='order-retrieve'),

    # Itens
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-retrieve-update-destroy'),
]
