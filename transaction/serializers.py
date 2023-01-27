from rest_framework import serializers
from .models import TRANSACTIONTYPECHOICES, Transaction


class InitializePaymentSerializer(serializers.Serializer):
    transaction_type = serializers.ChoiceField(
        choices=TRANSACTIONTYPECHOICES.choices,
    )
    price = serializers.DecimalField(max_digits=20, decimal_places=2)


class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "owner",
            "id",
            "transaction_type",
            "is_verified",
            "is_paid",
            "is_canceled",
            "total_price",
            "created_at",
        )

    def to_representation(self, instance):
        return super().to_representation(instance)
