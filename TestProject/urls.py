from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import ClientViewSet, OrganizationViewSet, BillViewSet


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'bills', BillViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
