from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authtoken.models import Token
from drf_spectacular.utils import extend_schema, extend_schema_view
from .utils import AuthUtils
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class UserLoginView(APIView):
    

    @extend_schema(
        request=LoginSerializer, responses={200: UserSerializer, 401: "Unauthorized"}
    )
    def post(self, request):
        auth_utils = AuthUtils()
        try:
            user, token = auth_utils.login(request)
            user_data = UserSerializer(user).data
            return Response({"user": user_data, "access_token": token.key}, status=200)
        except Exception as e:
            raise AuthenticationFailed(str(e))


class UserRegisterView(APIView):
    @extend_schema(
        request=RegisterSerializer, responses={201: UserSerializer, 400: "Bad Request"}
    )
    def post(self, request):
        auth_utils = AuthUtils()
        try:
            user, token = auth_utils.register(request)
            user_data = UserSerializer(user).data
            return Response({"user": user_data, "access_token": token.key}, status=200) 
        except Exception as e:
            raise APIException(str(e))


class UserLogoutView(APIView):
    @extend_schema(responses={200: "Logged out successfully"})
    def post(self, request):
        auth_utils = AuthUtils()
        auth_utils.logout(request)
        return Response({"detail": "Logged out successfully"}, status=200)
