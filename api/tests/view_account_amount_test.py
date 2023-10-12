from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


class ViewAccountAmount(APITestCase):
    def setUp(self):
        # Please notice that it is not good practice to use endpoints to setup tests
        # Since it break code isolation. I'm doing it to save time.
        self.client.post(f"/users/", {"username": "testuser"})

    def test_view_valid_account(self):
        """
        Ensure we can see an account, given that it exists.
        """
        response = self.client.get(f"/accounts/1/")

        self.assertIn("amount", response.json())

    def test_view_invalid_account(self):
        """
        Ensure we cannot see an account, given that it doesn't exists.
        """
        response = self.client.get(f"/accounts/-1/")

        self.assertEqual(response.status_code, 404)
