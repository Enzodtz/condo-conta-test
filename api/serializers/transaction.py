from rest_framework import serializers
from api.models import Transaction, Account


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ("payer_amount_after", "receiver_amount_after")

    def create(self, validated_data):
        payer: Account = validated_data["payer"]
        receiver: Account = validated_data["receiver"]
        amount = validated_data["amount"]

        payer.amount -= amount
        receiver.amount += amount

        payer.save()
        receiver.save()

        transaction = Transaction(
            payer=payer,
            receiver=receiver,
            amount=amount,
            payer_amount_after=payer.amount,
            receiver_amount_after=receiver.amount,
            description=validated_data["description"],
        )

        transaction.save()

        return transaction
