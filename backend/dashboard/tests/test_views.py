from .test_setup import DashboardTestSetup
from django.contrib.auth.models import User


class Dashboard_test(DashboardTestSetup):
    def user_can_send_message_with_correct_data(self):
        User.objects.create_user(username=self.receiver_user['username'], password=self.receiver_user['password'])
        User.objects.create_user(username=self.sender_user['username'], password=self.sender_user['password'])
        response = self.client.post(self.message_url, self.correct_message)
        self.assertEqual(response.status_code, 200, "error")
