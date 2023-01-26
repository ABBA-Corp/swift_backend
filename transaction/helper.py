from paycomuz import Paycom
from .models import Transaction
from .service import pay_transaction, cancel_transaction
from django.conf import settings
from decimal import Decimal

converter_amount = settings.PAYME_PRICE_HELPER


class CheckPayMeTransaction(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        try:
            transaction = Transaction.objects.get(id=account['order_id'])
            """
            Note
            below we have amount / converter_amount
            the purpose of this is the following:
                - transaction total price is in uzb sums
                - PayMe returns price in TIYN
                - if we have 10 000 sums in transaction payme sends it as 1 000 000 tiyns
                - that's why we have to divide Payme price by 100 to convert it into sums    
            """

            if transaction.total_price != amount / converter_amount:
                return self.INVALID_AMOUNT
            transaction.verify()
        except Transaction.DoesNotExist:
            return self.ORDER_NOT_FOND
        return self.ORDER_FOUND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        pay_transaction(transaction.order_key)

    def cancel_payment(self, account, transaction, *args, **kwargs):
        cancel_transaction(transaction.order_key)