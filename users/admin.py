from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

admin.site.register()

TokenAdmin.raw_id_fields = ['user']