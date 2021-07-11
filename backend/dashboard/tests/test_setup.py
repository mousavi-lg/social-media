from rest_framework.test import APITestCase
from django.urls import reverse


class DashboardTestSetup(APITestCase):
    def setUp(self):
        self.message_url = reverse('message')
        
        self.sender_user = {
            'username': 'senderusername',
            'password': 'senderpassword'
        }
        self.receiver_user = {
            'username': 'receiverusername',
            'password': 'receiverpassword'
        }
        self.correct_message = {
            'receiver': '2',
            'message': 'hello'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
