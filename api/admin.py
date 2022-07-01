from django.contrib import admin
from .models import Client, Organization


admin.site.register(Client)
admin.site.register(Organization)
