from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ClientViewSet, OrganizationViewSet, BillViewSet, PopulateDatabaseView


router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'bills', BillViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('populate-database', PopulateDatabaseView.as_view(), name='populate_database')
]