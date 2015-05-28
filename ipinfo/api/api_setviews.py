from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser

from rest_framework.decorators import detail_route, list_route

from .models import *
from .serializers import *


class PlaceViewSet(viewsets.ModelViewSet):

    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


class Ip_InfoViewSet(viewsets.ModelViewSet):

    serializer_class = Ip_InfoSerializer
    queryset = Ip_Info.objects.all()


class Project_InfoViewSet(viewsets.ModelViewSet):

    serializer_class = Project_InfoSerializer
    queryset = Project_Info.objects.all()


class Database_AddrViewSet(viewsets.ModelViewSet):

    serializer_class = Database_AddrSerializer
    queryset = Database_Addr.objects.all()


class Database_ConnViewSet(viewsets.ModelViewSet):

    serializer_class = Database_ConnSerializer
    queryset = Database_Conn.objects.all()


class Database_InfoViewSet(viewsets.ModelViewSet):

    serializer_class = Database_InfoSerializer
    queryset = Database_Info.objects.all()


class Login_ModeViewSet(viewsets.ModelViewSet):

    serializer_class = Login_ModeSerializer
    queryset = Login_Mode.objects.all()


class Log_SaveViewSet(viewsets.ModelViewSet):

    serializer_class = Log_SaveSerializer
    queryset = Log_Save.objects.all()
