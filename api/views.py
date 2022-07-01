from rest_framework.viewsets import ModelViewSet

from .models import Client, Organization
from .serializers import ClientSerializer, OrganizationSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
