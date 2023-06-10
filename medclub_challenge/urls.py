from django.urls import include, path
from django.contrib import admin

urlpatterns = [

    # Administração do Django
    path('admin/', admin.site.urls), 

    # App Users
    path('users/', include("users.urls")),

    # App Orders
    path('', include("orders.urls")),

]