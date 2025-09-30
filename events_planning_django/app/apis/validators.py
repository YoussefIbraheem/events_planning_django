from app.models import CustomUser


class UserLoginValidator:

    @staticmethod
    def validate(data):
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            raise ValueError("Username and password are required")
        if not CustomUser.objects.filter(username=username).exists():
            raise ValueError("User does not exist")
        
        return data


class UserRegisterValidator:

    @staticmethod
    def validate(data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        password2 = data.get("password2")
        if not username or not email or not password or not password2:
            raise ValueError("All fields are required")
        if password != password2:
            raise ValueError("Passwords do not match")
        if CustomUser.objects.filter(username=username).exists():
            raise ValueError("Username already exists")
        if CustomUser.objects.filter(email=email).exists():
            raise ValueError("Email already exists")
        return data
