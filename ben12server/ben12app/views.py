from datetime import datetime

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *


class ClientAPIView(GenericAPIView):
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs) -> Response:
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs) -> Response:
        data = {
            'id': get_last_client_id() + 1,
            'name': request.data.get('name'),
            'date_of_birth': request.data.get('date_of_birth'),
            'date_created': datetime.now(),
            'address': request.data.get('address')
        }
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailView(GenericAPIView):
    serializer_class = ClientSerializer

    def get_client(self, client_id: int) -> Client or None:
        try:
            return Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return None

    def get(self, request, client_id: int, *args, **kwargs) -> Response:
        client_instance = self.get_client(client_id)
        if not client_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, client_id: int, *args, **kwargs) -> Response:
        client_instance = self.get_client(client_id)
        if not client_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        client_instance.delete()
        return Response(status=status.HTTP_200_OK)
