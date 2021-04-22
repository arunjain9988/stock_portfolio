from django.db import models
from django.shortcuts import get_object_or_404
import requests

# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

class Customer(models.Model):
    NAME_PREFIX_CHOICES = [
        ('A','Mr'),
        ('C','Miss'),
        ('B','Mrs'),
    ]
    name_prefix = models.CharField(max_length=1,choices=NAME_PREFIX_CHOICES)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.ForeignKey(Address,on_delete=models.PROTECT)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=100,null=True)
    def full_name(self):
        return self.get_name_prefix_display() + ' ' + self.fname+ ' '+  self.lname
    def assets(self):
        values = Transaction.objects.filter(customer = self)
        # print('call')
        total = 0
        for v in values:
            total+=v.amount
        print(total)
        return str(total)

    def __str__(self):
        return self.full_name()

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=50)
    primary_exchange = models.CharField(max_length=50)
    def current_price(self):
        ret = requests.get("https://cloud.iexapis.com/stable/stock/T/quote/latestPrice",
        params={
            "token":"pk_d53d8b6d9e404d16baf23b3e51c46dbc",
        })
        # print(ret)
        return ret.json
    def is_market_open():
        ret = requests.get("https://cloud.iexapis.com/stable/stock/T/quote/isUSMarketOpen",
        params={
            "token":"pk_d53d8b6d9e404d16baf23b3e51c46dbc",
        })
        # print(ret)
        print(type(ret.json))
        return ret.json
    def __str__(self):
        return self.symbol


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('A','Buy'),
        ('B','Sell'),
    ]
    date = models.DateField(auto_now=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock,on_delete=models.CASCADE)
    amount = models.FloatField()
    quantity = models.FloatField()
    commision = models.FloatField()
    type = models.CharField(max_length=1,choices=TRANSACTION_TYPE_CHOICES)




