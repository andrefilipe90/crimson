# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import SalaSerializer
from .models import Sala


# Create your views here.
def main(request):
    return HttpResponse("<h1>Hello</h1>")

# def teste(request):
#     return HttpResponse("teste")

class SalaView(generics.ListAPIView):
    queryset = Sala.objects.all()
    serializer_class =  SalaSerializer

class SalaInsert(generics.CreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer