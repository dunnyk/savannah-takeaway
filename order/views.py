from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated, AllowAny
from helpers.send_customer_sms import send_sms

from .serializers import OrderSerializer, OrderGetUpdateDestroySerializer
from .models import Order

# Create your views here.


class OrderCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):

        phone_number = request.user.phone_number
        order = request.data
        serializer = self.serializer_class(data=order)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=request.user)

        # send and sms
        send_sms(phone_number)

        return_message = {
            "message": "your order is placed successfully",
        }
        return Response(return_message, status.HTTP_201_CREATED)

    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderGetUpdateDestroySerializer(queryset, many=True)
        data = serializer.data
        return_feedback = {
            "message": "You retrieved your orders successfully",
            "data": data
        }
        return Response(return_feedback, status.HTTP_200_OK)


class OrderGetUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderGetUpdateDestroySerializer

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(order)
        data = serializer.data
        return_feedback = {
            "message": "Order pulled successfully",
            "data": data
        }
        return Response(return_feedback, status.HTTP_200_OK)

    def patch(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        data = request.data
        serializer = self.serializer_class(order, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return_feedback = {
            "message": "You have updated your order successfully",
            "data": data
        }
        return Response(return_feedback, status.HTTP_201_CREATED)

    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        serializer = self.serializer_class(order)
        return_feedback = {
            "message": "Order deleted successfully",
        }
        return Response(return_feedback, status.HTTP_200_OK)
