from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Client


class ClientSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'url', 'name']
