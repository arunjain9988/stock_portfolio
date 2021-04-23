# from django.db import models
from django.contrib import admin
from transact.models import Customer,Transaction,Stock,Address


# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Stock)
admin.site.register(Address)
