from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import Pet, FinderFormsModel
from users.serializers import UserSerializer, FinderFormsSerializer, PetSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer

User = get_user_model()


@api_view(['GET'])
def main_api_view(request):
    """Метод проверки api"""
    return Response({
        'status': 'ok',
    })


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UsersViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.all()


class PetsViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        return PetSerializer

    def get_queryset(self):
        user = self.request.user
        return Pet.objects.select_related('owner')


class FinderFormsViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        return FinderFormsSerializer

    def get_queryset(self):
        user = self.request.user
        return FinderFormsModel.objects.select_related('user')


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer