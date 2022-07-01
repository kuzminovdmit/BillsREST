from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import ClientViewSet, OrganizationViewSet


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'organizations', OrganizationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
