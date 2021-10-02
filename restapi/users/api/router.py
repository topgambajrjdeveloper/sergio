from django.urls import path
from users.api.views import RegisterUserAPIView, UserAPIView, UserProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('auth/usuarios/', UserAPIView.as_view(), name='users'),
    path('auth/registro/', RegisterUserAPIView.as_view(), name='user_register'),
    path('auth/acceder/', TokenObtainPairView.as_view(), name='user_login'),
    path('auth/refrescar/token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/perfil/', UserProfileAPIView.as_view(), name='user_profile'),
]
