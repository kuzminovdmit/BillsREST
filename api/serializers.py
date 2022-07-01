from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Client, Organization


class ClientSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'url', 'name']


class OrganizationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'url', 'name', 'address', 'client']
