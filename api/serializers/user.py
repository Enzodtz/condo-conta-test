from django.contrib.auth.models import User
from rest_framework import serializers
from .account import AccountSerializer
from api.models import Account


class UserSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "accounts")

    def create(self, validated_data):
        """
        Overriding default creation method to create accounts.
        """
        user = super(UserSerializer, self).create(validated_data)

        saving_account = Account(
            user=user,
            type=Account.AccountType.SAVING,
            amount=1,
        )
        saving_account.save()

        checking_account = Account(
            user=user,
            type=Account.AccountType.CHECKING,
            amount=1000,
        )
        checking_account.save()

        return user
