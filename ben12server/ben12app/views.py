from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *


class ClientAPIView(APIView):
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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
