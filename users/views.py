from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, GroupSerializer


# Usuários


# Registro de um usuário
# POST /users/: Cria um novo usuário
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Requisições dos dados de um usuário autenticado
# GET PUT DELETE /users/<id>/ 
# Retorna, atualiza e exclui os dados do usuário com o ID fornecido
class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # Retorna apenas as informações do próprio usuário autenticado
    def get_object(self):
        return self.request.user


# Grupos de Usuários


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]