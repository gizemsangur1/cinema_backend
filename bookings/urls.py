from django.urls import path
from .views import SessionListCreateView, ReservationCreateView

urlpatterns = [
    path('sessions/', SessionListCreateView.as_view(), name='session-list-create'),
    path('reserve/', ReservationCreateView.as_view(), name='reservation-create'),
]
