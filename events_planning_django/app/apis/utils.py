from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from app.models import CustomUser
from .validators import UserLoginValidator, UserRegisterValidator


class AuthUtils:

    def login(self, request):

        validated_data = UserLoginValidator.validate(request.data)
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = authenticate(request, username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return user, token

    def register(self, request):
        validated_data = UserRegisterValidator.validate(request.data)
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = CustomUser.objects.create_user(
            username=username, email=email, password=password
        )
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return user, token

    def logout(self, request):
        logout(request)
        return True
