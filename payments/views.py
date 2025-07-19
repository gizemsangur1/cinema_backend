from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from bookings.models import Reservation

class MakePaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        reservation_id = request.data.get("reservation")
        amount = request.data.get("amount")

        try:
            reservation = Reservation.objects.get(id=reservation_id, user=request.user)
            if reservation.is_paid:
                return Response({"error": "Already paid."}, status=400)

            payment = Payment.objects.create(reservation=reservation, amount=amount)
            reservation.is_paid = True
            reservation.save()

            serializer = PaymentSerializer(payment)
            return Response(serializer.data, status=201)
        except Reservation.DoesNotExist:
            return Response({"error": "Reservation not found."}, status=404)
