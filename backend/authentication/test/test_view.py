from django.http import request, response
from .test_setup import TestSetUp
from django.contrib.auth.models import User


class TestViews(TestSetUp):
    def test_user_can_login_with_correct_data(self):
        User.objects.create_user(username=self.correct_login_data['username'],
        password=self.correct_login_data['password'])
        response = self.client.post(self.login_url, self.correct_login_data)
        self.assertEqual(response.status_code, 200, "error")

    def test_user_can_login_with_incorrect_data(self):
        User.objects.create_user(username=self.correct_login_data['username'],
        password=self.correct_login_data['password'])
        response = self.client.post(self.login_url, self.incorrect_login_data)
        self.assertEqual(response.status_code, 401, "error")

    def test_user_can_login_with_no_data(self):
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, 500, "error")

    def test_user_can_logout_with_correct_data(self):
        User.objects.create_user(username=self.correct_login_data['username'], password=self.correct_login_data['password'])
        self.client.login(username=self.correct_login_data['username'], password=self.correct_login_data['password'])
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200, "error")

    def test_user_can_logout_with_incorrect_data(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 403, "error")

    def test_user_can_register_with_correct_data(self):
        response = self.client.post(self.register_url, self.correct_register_data)
        self.assertEqual(response.status_code, 201, "error")

    def test_user_can_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400, "error")