from .models import Transaction


def initialize_transaction(fullname, phone, price, transaction_type):
    obj = Transaction.objects.create(
        fullname=fullname,
        phone=phone,
        total_price=price,
        transaction_type=transaction_type,
    )
    return obj.id


def pay_transaction(transaction_id):
    try:
        instance = Transaction.objects.get(id=transaction_id)
        instance.make_payment()
    except Transaction.DoesNotExist:
        return


def cancel_transaction(transaction_id):
    try:
        instance = Transaction.objects.get(id=transaction_id)
        instance.cancel()
    except Transaction.DoesNotExist:
        return