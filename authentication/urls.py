from django.urls import path
from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('customers/', RegistrationAPIView.as_view(), name='customers-signup'),
    path('login/', LoginAPIView.as_view(), name='customer-login')
]
