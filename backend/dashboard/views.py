from typing import cast
from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message, Profile
from rest_framework import status

class MessageView(APIView):
    def post(request, self):
        message = Message(
            sender = request.user,
            receiver = int(request.data['receiver']),
            message = request.data['message']
        )
        if message is not None:
            message.save() 
            return Response({"message": "saved"})
        else:
            return Response({"message":"something unexpected heppened"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProfileView(models.Model):
    def get(request, self):
        profile = Profile.objects.get(user=request.user)
        return Response({"profile": profile.profile})
    def put(request, self):
        profile = Profile.objects.get(user=request.user)
        profile.profile = request.data['profile']
        profile.save()
        return Response({"profile": profile.profile})
    def post(request, self):
        profile = Profile.objects.get(user=request.user)
        profile.profile = request.data['profile']
        profile.save()
        return Response({"profile": profile.profile})
    def delete (request, self):
        profile = Profile.objects.get(user=request.user)
        profile.remove()
        return Response({"profile": "profile has been removed"})
