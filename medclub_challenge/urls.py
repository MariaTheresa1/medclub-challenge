from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    # Rotas
    path('', include(router.urls)),

    # Administração do Django
    path('admin/', admin.site.urls), 

    # App Users
    path('users/', include("users.urls")),

]