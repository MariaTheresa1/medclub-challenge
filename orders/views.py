from rest_framework import generics
from .models import Order, Item
from .serializers import OrderSerializer, ItemSerializer
from rest_framework.permissions import IsAuthenticated


# Pedidos


# POST - orders/
# Criar um pedido (apenas usuário autenticado)
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# GET, PUT, PATCH, DELETE - orders/<id>
# Recuperar, atualizar e excluir um pedido (apenas usuário autenticado)
class OrderRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)


# Itens


# POST - items/
# Criar um item 
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# GET, PUT, PATCH, DELETE - items/<id>/
# Recuperar, atualizar e excluir um item
class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
