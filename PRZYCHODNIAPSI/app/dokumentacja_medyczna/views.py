from django.shortcuts import render
from .models import Dokumentacja_medyczna
from .serializers import Dokumentacja_medycznaSerializer
from rest_framework import viewsets


# Create your views here.

class Dokumentacja_medycznaViewSet(viewsets.ModelViewSet):
    queryset = Dokumentacja_medyczna.objects.all()
    serializer_class = Dokumentacja_medycznaSerializer
