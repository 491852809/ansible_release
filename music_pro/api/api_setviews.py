from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser

from rest_framework.decorators import detail_route, list_route

from .models import *
from .serializers import *



class MusicViewSet(viewsets.ModelViewSet):

    serializer_class = MusicSerializer
    queryset = Music.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
