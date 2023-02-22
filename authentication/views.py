
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


from .serializers import RegistrationSerializer, LoginSerializer
from .models import User

# Create your views here.


class RegistrationAPIView(generics.CreateAPIView):
    '''allow any user to hit this endpoint'''
    permission_classed = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        '''handle user registration'''
        user = request.data
        serialiazer = self.serializer_class(data=user)
        serialiazer.is_valid(raise_exception=True)
        serialiazer.save()
        return Response(serialiazer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.CreateAPIView):
    '''
        Hit this endpoint, only if you have logged in.
    '''
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        """Handle user login
        """
        # breakpoint()
        # self.request.user.token.decode('utf-8')
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
