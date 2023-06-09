from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.views import UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [

    path('api-token-auth/', obtain_auth_token),

    path('', UserCreateView.as_view(), name='user-create'),

    path(
        '<int:pk>/', 
        UserRetrieveUpdateDestroyView.as_view(), 
        name='user-retrieve-update-destroy'
        ),    
]