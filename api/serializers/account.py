from rest_framework import serializers
from api.models import Account
from .transaction import TransactionSerializer


class AccountSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id")
    expenses = TransactionSerializer(many=True, read_only=True)
    revenues = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ["id", "type", "amount", "user_id", "expenses", "revenues"]
