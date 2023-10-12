from django.db import models
from .account import Account


class Transaction(models.Model):
    payer = models.ForeignKey(
        Account,
        related_name="expenses",
        on_delete=models.PROTECT,
    )
    receiver = models.ForeignKey(
        Account,
        related_name="revenues",
        on_delete=models.PROTECT,
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)

    payer_amount_after = models.DecimalField(max_digits=10, decimal_places=2)
    receiver_amount_after = models.DecimalField(max_digits=10, decimal_places=2)
