from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response


class SelectUser(APIView):
    def post(self, request):
        username = request.data['selected_username']
        user = bool(User.objects.get(username = username))
        if user:
            return Response("That username exists.")


