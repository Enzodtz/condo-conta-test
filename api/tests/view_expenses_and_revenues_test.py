from rest_framework.test import APITestCase


class ViewAccountTransactions(APITestCase):
    def setUp(self):
        # Please notice that it is not good practice to use endpoints to setup tests
        # Since it break code isolation. I'm doing it to save time.
        self.client.post(f"/users/", {"username": "testuser"})
        self.client.post(f"/transactions/", {"payer": 2, "receiver": 1, "amount": 5})

    def test_view_transactions_valid_account(self):
        """
        Ensure we can see transactions with right fields, given that the account exists.
        """
        response = self.client.get(f"/accounts/1/")
        json = response.json()

        for field in ["expenses", "revenues"]:
            self.assertIn(field, json)
            for register in json[field]:
                for subfield in [
                    "datetime",
                    "description",
                    "amount",
                    "payer_amount_after",
                    "receiver_amount_after",
                ]:
                    self.assertIn(subfield, register)

    def test_view_transactions_invalid_account(self):
        """
        Ensure we cannot see transactions, given that account doesn't exists.
        """
        response = self.client.get(f"/accounts/-1/")

        self.assertEqual(response.status_code, 404)
