from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer


class RegisterUserAPIView(APIView):
    """
    Register and create a new User.
    
    ### Along with **POST** request
        username: string
        first_name: string
        last_name: string
        password: string
        password2: string
    """
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"status": "OK", "message": "Registration Success!"}, status=status.HTTP_201_CREATED)
        print(serializer.data) # testing purpose
        return Response({"status": "NO", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(APIView):
    """
    Login User.
    
    ### Along with **POST** request
        email: string 
        password: string
    """
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            print(email, password) # testing
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                userSerializer = UserSerializer(user, many=False)
                return Response({"status": "OK", "message": "Login success!", "user": userSerializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "NO", "message": "Incorrect Password!"}, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['POST'])
def logout_view(request):
    """
    Logout User.
    """
    logout(request)
    return Response("Logout !")

