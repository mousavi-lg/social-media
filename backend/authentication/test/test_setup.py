from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self):
        self.login_url = reverse("login")
        self.register_url = reverse("register")
        self.logout_url = reverse("logout")

        self.correct_login_data = {
            'username' : 'randomusername',
            'password' : 'randompassword'
        }
        self.incorrect_login_data = {
            'username' : 'incorrectusername',
            'password' : 'incorrctpassword'
        }
        self.correct_register_data = {
            'username':'randomusername',
            'password':'randompassword',
            're_password':'randompassword',
            'email':'random@example.com'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

