from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    class AccountType(models.IntegerChoices):
        SAVING = 0
        CHECKING = 1

    user = models.ForeignKey(User, related_name="accounts", on_delete=models.PROTECT)
    type = models.IntegerField(
        choices=AccountType.choices,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
