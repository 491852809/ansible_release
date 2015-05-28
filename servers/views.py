from django.shortcuts import render

from rest_framework import generics,permissions,renderers
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser

from .models import *
from .serializers import *
from django.contrib.auth import authenticate
# Create your views here.

class Servers_InfoList(generics.ListCreateAPIView):
    queryset = Servers_Info.objects.all()
    serializer_class = Servers_InfoSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self,request,*args,**kwargs):
        response = super(Servers_InfoList,self).list(request,*args,**kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='server_info.html')
        return response

class Servers_InfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servers_Info.objects.all()
    serializer_class = Servers_InfoSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    lookup_field = 'eth1'

    def get(self,request,*args,**kwargs):
        response = super(Servers_InfoDetail,self).get(request,*args,**kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='server_detail.html')
        return response

class Test(generics.ListCreateAPIView):
    queryset = Servers_Info.objects.all()
    serializer_class = Servers_InfoSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self,request,*args,**kwargs):
        response = super(Test,self).list(request,*args,**kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='test.html')
        return response
