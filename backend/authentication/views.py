from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth.models import User

class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            return Response({"message":"user authenticated"})
        else:
            return Response({"message":"username or password is incorrect"})

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        re_password = data['re_password']
        email = data['email']
        if password == re_password:
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response({"message":"user created"})
        else:
            return Response({"message":"passwords dosen't match"})

class LogoutView(APIView):
    
    def get(self, request):
        auth.logout(request)
        return Response({"messgae":"user loged out"})