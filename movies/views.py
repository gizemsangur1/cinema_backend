from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
