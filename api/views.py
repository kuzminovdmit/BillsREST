from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Client, Organization, Bill
from .serializers import ClientSerializer, OrganizationSerializer, BillSerializer
from .services import populate_client_table, populate_organization_table, populate_bills_table


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filterset_fields = ['organization', 'client']


class PopulateDatabaseView(APIView):

    def get(self, request):
        return Response({
            'message': 'Необходимо сделать POST запрос без содержимого, чтобы извлечь данные из Excel-файлов и '
                       'заполнить ими базу данных'
        })

    def post(self, request):
        populate_client_table()
        populate_organization_table()
        populate_bills_table()

        return Response({
            'message': 'Успешно добавлены в базу данных из Excel-файлов клиенты, организации и счета',
        })
