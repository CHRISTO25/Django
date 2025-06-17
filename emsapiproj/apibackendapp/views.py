from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Employee,Department
from .serializers import EmployeeSerializer,DepartmentSerializer,LoginSerializer,UserSerializer
from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "status": status.HTTP_200_OK,
                    "message": "success",
                    "token": token.key,
                    "data": {
                        "Token": token.key
                    }
                })
            else:
                return Response({
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid Username or password",
                })
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Bad request - invalid input data",
                "errors": serializer.errors
            })
        
class UserDetailView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)