# from django.db import models
# from django.db.models.deletion import PROTECT
# import requests
# import json

# # Create your models here.
# class Customer(models.Model):
#     fname = models.CharField(max_length=200)
#     lname = models.CharField(max_length=200)
#     primary_email = models.CharField(max_length=100)
#     secondary_email = models.CharField(max_length=100)
#     address = models.CharField(max_length=200,default=None)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     pincode = models.CharField(max_length=10)
#     mobile = models.CharField(max_length=12)
#     created_date = models.DateField(auto_now=True)
#     modified_date = models.DateField(auto_now_add=True)
#     promotional_emails = models.BooleanField(null=True,default=False)
#     transactional_emails = models.BooleanField(null=True,default=False)
#     promotional_sms = models.BooleanField(null=True,default=False)
#     transactional_sms = models.BooleanField(null=True,default=False)
#     def __str__(self):
#         return self.fname+" "+self.lname
    
#     def name(self):
#         return self.fname+" "+self.lname

#     def short(self):
#         return self.fname[0]+self.lname[0]

#     def ID(self):
#         return self.short()+str(self.pk)

#     def fullAddress(self):
#         return self.address + ' ' + self.city + ' ' + self.state + ' ' + self.country

# class Stock(models.Model):
#     symbol = models.CharField(max_length=20,primary_key=True)
#     name = models.CharField(max_length=50)
#     def current_price(self):
#         url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + self.symbol + "&interval=5min&apikey=OA8OLUQDR9KVARZH"
#         response = requests.get(url)
#         js = response.text
#         dct = json.loads(js)
#         price = dct['Time Series (5min)'][dct['Meta Data']['3. Last Refreshed']]['4. close']
#         return price

# class Transaction(models.Model):
#     TRANSACTION_TYPE_CHOICES = [
#         ('A', 'Buy'),
#         ('B', 'Sell'),
#     ]
#     customer = models.ForeignKey(Customer,on_delete=PROTECT)
#     stock = models.ForeignKey(Stock,on_delete=PROTECT)
#     type = models.CharField(max_length=1,choices=TRANSACTION_TYPE_CHOICES)
#     date = models.DateField(auto_now=True)