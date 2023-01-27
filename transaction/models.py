from django.db import models
from django.conf import settings
from django.contrib.auth.models import User




class BaseManager(models.Manager):
    def get_queryset(self):
        return models.QuerySet(self.model)


class TRANSACTIONTYPECHOICES(models.TextChoices):
    PAYME = "payme"


class TRANSACTIONSTATUS(models.TextChoices):
    NEW = "new"
    VERIFIED = "verified"
    PAID = "paid"
    CANCELED = "canceled"
    ACCEPTED = "accepted"



class Transaction(models.Model):
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    is_verified = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='transactions')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTIONTYPECHOICES.choices,
    )
    status = models.CharField(
        max_length=10,
        choices=TRANSACTIONSTATUS.choices,
        default=TRANSACTIONSTATUS.NEW
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def verify(self):
        self.status = TRANSACTIONSTATUS.VERIFIED
        self.is_verified = True
        self.save()

    def make_payment(self):
        self.status = TRANSACTIONSTATUS.PAID
        self.is_paid = True
        self.save()

    def cancel(self):
        self.status = TRANSACTIONSTATUS.CANCELED
        self.is_canceled = True
        self.is_paid = False
        self.save()

    def __str__(self):
        return f"{str(self.owner)}  {str(self.total_price)}"

