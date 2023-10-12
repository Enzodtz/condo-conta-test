from rest_framework.test import APITestCase


class SavingToCheckingAccountTransaction(APITestCase):
    def setUp(self):
        # Please notice that it is not good practice to use endpoints to setup tests
        # Since it break code isolation. I'm doing it to save time.
        self.client.post(f"/users/", {"username": "testuser"})

    def test_view_transactions_valid_account(self):
        """
        Ensure we can do the transaction if the account exists.
        """
        # Notice that id 2 is the CHECKING account and 1 SAVING
        response = self.client.post(
            f"/transactions/",
            {
                "payer": 1,
                "receiver": 2,
                "amount": 1,
                "description": "test transaction",
            },
        )

        self.assertEqual(response.status_code, 201)

    def test_view_transactions_invalid_account(self):
        """
        Ensure we cannot do transactions, given that account doesn't exists.
        """
        response = self.client.post(
            f"/transactions/",
            {
                "payer": 3,
                "receiver": 3,
                "amount": 0,
                "description": "test transaction",
            },
        )

        self.assertEqual(response.status_code, 400)
