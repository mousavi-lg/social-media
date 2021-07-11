from typing import cast
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message
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

