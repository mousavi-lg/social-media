from django.core.checks import messages
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework import status

class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data
            username = data['username']
            password = data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                return Response({"message":"user authenticated"})
            else:
                return Response({"message":"username or password is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({"message":"something unexpected heppened"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        data = request.data
        try:
            username = data['username']
            password = data['password']
            re_password = data['re_password']
            email = data['email']
            if password == re_password:
                user = User.objects.create_user(username=username, password=password, email=email)
                return Response({"message":"user created"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"passwords dosen't match"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message":"somethings went wrong"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    
    def get(self, request):
        auth.logout(request)
        return Response({"messgae":"user loged out"})