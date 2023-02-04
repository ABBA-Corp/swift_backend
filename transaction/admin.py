from django.contrib import admin

from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "transaction_type",
        "status",
        "phone",
        "fullname",
        "is_paid",
        "is_verified",
        "is_canceled",  
    )
    list_display_links = ("id",)
    list_filter = (
        "status",
        "transaction_type",
        "is_paid",
        "is_verified",
        "is_canceled",
    )
    search_fields = [
        "fullname",
    ]
    list_editable = ("is_paid", "transaction_type", "status")


admin.site.register(Transaction, TransactionAdmin)
