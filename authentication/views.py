from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics, viewsets, status, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import *
from django.shortcuts import get_object_or_404
import requests

class LoginAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginAPISerializer
    http_method_names = ['get', 'post']
    def get(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        Token.objects.get(user=self.request.user).delete()
        return Response({'message': 'User is logged out'})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = User.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = UserSerializer
  http_method_names = ['get', 'head']
  


class RegisterUserAPIView(generics.CreateAPIView):  
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  def get(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
  search_fields = ['city']
  filterset_fields = ['tags', 'post_type', 'city', 'room_number', ]
  ordering_fields = ['price']
  http_method_names = ['get', 'head']

class ReviewViewSet(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['post']
  http_method_names = ['get', 'head']

class SavedPostViewSet(viewsets.ModelViewSet):
  queryset = SavedPost.objects.all()
  serializer_class = SavedPostSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['user']
  http_method_names = ['get', 'head']