from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token


# Usuários


# Registro de um usuário
# POST /users/: Cria um novo usuário
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


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

