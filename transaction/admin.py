from django.contrib import admin
from .models import Order
from django.contrib.auth.models import Group, User

# Register your models here.


admin.site.register(Order)


admin.site.site_header = 'Payment Administration'

admin.site.unregister(Group)