from django.shortcuts import render

from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def ip_info_add(request):
    if request.method == 'GET':
        return render(request, 'ip_info_add.html')

@api_view(['GET', 'POST'])
def ip_add_place(request):
    if request.method == 'GET':
        return render(request, 'ip_add_place.html')

@api_view(['GET', 'POST'])
def ip_info_main(request):
    if request.method == 'GET':
        return render(request, 'ip_info_main.html')
