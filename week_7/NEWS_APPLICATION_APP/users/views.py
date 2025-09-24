from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, AuthorSerializer
from .models import Author    

# Authentication imports
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiExample

# Create your views here.

@extend_schema(
        summary="To Register a User",
        request=dict,
        examples= [
            OpenApiExample(
                name="Register User",
                value={
                    "first_name": "first name here",
                    "last_name": "last name here",
                    "email": "email here",
                    "password": "password here",
                    "role": "role here"
                },      
            )
        ]
)
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_200_OK)  
    else:
        return Response({"message": "Something went wrong", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  


@extend_schema(
        summary="To Login the User",
        request=dict,
        examples= [
            OpenApiExample(
                name="Login User",
                value={
                    "email": "email here",
                    "password": "password here"
                },      
            )
        ]
)
@api_view(["POST"]) 
@permission_classes([permissions.AllowAny])   
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

#   looking for user in the database   
    user = authenticate(email=email, password=password)  

    if user is not None: 
        access = AccessToken.for_user(user) 
        refresh = RefreshToken.for_user(user)   
        return Response({"message": "User logged in successfully", "access_token": str(access), "refresh_token": str(refresh)}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Your username or password is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(["POST"])
def create_author(request):
    if Author.objects.filter(user=request.user).exists():
        return Response(
            {"message": "Author data already exists for this user"}, status=status.HTTP_400_BAD_REQUEST)
    
    author_data = request.data
    serializer = AuthorSerializer(data=author_data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"message": "Author data created successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Something went wrong", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)