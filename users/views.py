from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegisterSerializer, UserLoginSerializer


class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"status": "OK", "message": "Registration Success!"}, status=status.HTTP_201_CREATED)
        return Response({"status": "NO", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email, password)
            if user is not None:
                login(request, user)
                return Response({"status": "OK", "message": "Login success!"}, status=status.HTTP_200_OK)
        return Response({"status": "NO", "message": "Incorrect Password!"}, status=status.HTTP_400_BAD_REQUEST)
            

@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)

