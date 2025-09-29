from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from app.models import CustomUser


class AuthUtils:

    def login(request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return user, token
        return None, None

    def register(request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        if CustomUser.objects.filter(username=username).exists():
            return None, None
        user = CustomUser.objects.create_user(
            username=username, email=email, password=password
        )
        token, _ = Token.objects.get_or_create(user=user)
        return user, token

    def logout(request):
        user = request.user
        logout(request, user)
