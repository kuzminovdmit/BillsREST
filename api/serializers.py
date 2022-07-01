from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Client, Organization, Bill


class ClientSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'url', 'name']


class OrganizationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'url', 'name', 'address', 'client', 'fraud_weight']


class BillSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Bill
        fields = [
            'id', 'url', 'organization', 'client_number', 'client',
            'sum', 'date', 'fraud_score', 'service_class', 'service_name'
        ]
