from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import permissions

from rest_framework.status import HTTP_409_CONFLICT
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class ResearcherUserViewSet(viewsets.ModelViewSet):
    queryset = ResearcherUser.objects.all()
    serializer_class = ResearcherUserSerializer
    permission_classes = (permissions.IsAdminUser,)


class ManagerUserViewSet(viewsets.ModelViewSet):
    queryset = ManagerUser.objects.all()
    serializer_class = ManagerUserSerializer
    permission_classes = (permissions.IsAdminUser,)
