from django.shortcuts import render

from rest_framework import generics
from .models import Hall
from .serializers import HallSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

