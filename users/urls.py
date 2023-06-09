from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.views import UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [

    # Retorna o token de um usuário 
    path('api-token-auth/', obtain_auth_token),

    # Permite a criação de um usuário (POST) sem a necessidade de altenticação
    path('', UserCreateView.as_view(), name='user-create'),

    # Permite o GET, PUTH, PATCH e DELETE de um usuário autenticado
    path(
        '<int:pk>/', 
        UserRetrieveUpdateDestroyView.as_view(), 
        name='user-retrieve-update-destroy'
        ),    
]