from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from users.models import User
from users.api.serialiezer import UserRegisterSerializer, UserProfileSerializer, UserUpdateProfileSerializer


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = [usuarios.username for usuarios in User.objects.all()]
        return Response(status=status.HTTP_200_OK, data=users)


class RegisterUserAPIView(APIView):
    def post(self, request):
        registro = UserRegisterSerializer(data=request.data)
        if registro.is_valid(raise_exception=True):
            registro.save()
            return Response(registro.data)
        return Response(registro.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        get_user = UserProfileSerializer(request.user)
        return Response(get_user.data, status=status.HTTP_200_OK)

    def put(self, request):
        user_profile = User.objects.get(request.user.id)
        update_user = UserUpdateProfileSerializer(user_profile, request.data)
        if update_user.is_valid(raise_exception=True):
            update_user.save()
            return Response(update_user.data)
        return Response(update_user.errors, status=status.HTTP_400_BAD_REQUEST)
