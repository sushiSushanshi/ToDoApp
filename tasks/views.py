from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import Task
from .serializer import TaskSerializer


# Create your views here.

@api_view(['GET'])
def hello_world(request):
    return HttpResponse("Hello world from function view")

class HelloWorld(View):
    def get(self, request):
        return HttpResponse("Hello world from class view ")

class Tasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
