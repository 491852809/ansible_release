from django.shortcuts import render


from rest_framework import generics,permissions,renderers
from rest_framework.response import Response

from api.models import *
from api.serializers import *
from api.api_setviews import *


# deploy page function

from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def mainpage(request):
    if request.method == 'GET':
        return render(request, 'setgame.html')

@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'GET':
        return render(request, 'test.html')

