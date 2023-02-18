from django.db import models

from django.conf import settings
from authentication.models import User



class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
