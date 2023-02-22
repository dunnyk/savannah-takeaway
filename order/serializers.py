
from django.conf import settings
from rest_framework import serializers
from .models import Order, User
from authentication.serializers import UserRetrieveSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ['customer', 'item', 'amount', 'create_at']


class OrderGetUpdateDestroySerializer(serializers.ModelSerializer):

    customer = serializers.SerializerMethodField()

    @staticmethod
    def get_customer(obj):
        customer_obj = User.objects.get(id=obj.customer.id)
        serializer = UserRetrieveSerializer(customer_obj)
        return serializer.data

    class Meta:
        model = Order
        fields = ['customer', 'item', 'amount']
