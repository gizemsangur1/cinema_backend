from django.urls import path
from .views import HallListCreateView

urlpatterns = [
    path('', HallListCreateView.as_view(), name='hall-list-create'),
]
