from django.urls import path
from .views import OrderCreateListView, OrderGetUpdateDestroyView

urlpatterns = [
    path('orders/', OrderCreateListView.as_view(), name='orders'),
    path('retrieve/<str:order_id>', OrderGetUpdateDestroyView.as_view(), name='retrieve')
]
