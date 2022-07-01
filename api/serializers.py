from rest_framework.serializers import HyperlinkedModelSerializer, ReadOnlyField

from .models import Client, Organization, Bill


class ClientSerializer(HyperlinkedModelSerializer):
    organizations_count = ReadOnlyField()
    organizations_income = ReadOnlyField()

    class Meta:
        model = Client
        fields = ['id', 'url', 'name', 'organizations_count', 'organizations_income']


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
