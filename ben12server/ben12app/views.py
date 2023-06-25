from datetime import datetime

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class ClientGeneralView(GenericAPIView):
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


def get_client(client_id: int) -> Client or None:
    try:
        return Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return None


class ClientDetailView(GenericAPIView):
    serializer_class = ClientSerializer

    def get(self, request, client_id: int, *args, **kwargs) -> Response:
        client_instance = get_client(client_id)
        if not client_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, client_id: int, *args, **kwargs) -> Response:
        client_instance = get_client(client_id)
        if not client_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        client_instance.delete()
        return Response(status=status.HTTP_200_OK)


class RecordDetailView(GenericAPIView):
    serializer_class = RecordSerializer

    def get(self, request, client_id: int, how_many: int = 10, *args, **kwargs) -> Response:
        client_instance = get_client(client_id)
        if not client_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            records = Record.objects.filter(client=client_instance)[:how_many]
        except Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, client_id: int, *args, **kwargs) -> Response:
        data = {
            'client': client_id,
            'heartbeat': request.data.get('heartbeat'),
            'blood_oxygen_level': request.data.get('blood_oxygen_level'),
            'alcohol_level': request.data.get('alcohol_level'),
            'date_time_recording': request.data.get('date_time_recording'),
            'date_time_sent': datetime.now()
        }

        serializer = RecordSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_specific(self, request, client_id: int, record_id: int, *args, **kwargs) -> Response:
        client_instance = get_client(client_id)
        if not client_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            records = Record.objects.get(client=client_instance, id=record_id)
        except Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecordSerializer(records)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecordAlcoholView(GenericAPIView):
    serializer_class = RecordSerializer

    def get(self, request, client_id: int, *args, **kwargs):
        client_instance = get_client(client_id)
        if not client_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            records = Record.objects.last()
        except Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        alcohol = getattr(records, 'alcohol_level')
        response = Response(status=status.HTTP_200_OK)
        response['alcohol_value'] = alcohol
        return response


class RecordHeartbeatView(GenericAPIView):
    serializer_class = RecordSerializer

    def get(self, request, client_id: int, *args, **kwargs):
        client_instance = get_client(client_id)
        if not client_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            records = Record.objects.last()
        except Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        heartbeat = getattr(records, 'heartbeat')
        response = Response(status=status.HTTP_200_OK)
        response['heartbeat_value'] = heartbeat
        return response
