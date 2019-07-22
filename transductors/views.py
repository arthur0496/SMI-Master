import json

from django.shortcuts import render

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets, permissions

from .api import *
from slaves.models import Slave
from .models import EnergyTransductor
from .serializers import EnergyTransductorSerializer


class EnergyTransductorViewSet(viewsets.ModelViewSet):
    queryset = EnergyTransductor.objects.all()
    serializer_class = EnergyTransductorSerializer
    permission_classes = (permissions.AllowAny,)

    @action(detail=True, methods=['post'])
    def add_to_server(self, request, pk=None):
        slave_server = Slave.objects.get(id=request.data["slave_id"])
        response = self.get_object().create_on_server(slave_server)
        return Response(data=json.loads(response.content), status=response.status_code)
