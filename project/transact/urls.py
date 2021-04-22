from django.urls import path
from . import views

urlpatterns = [
    path('',views.transactions,name='transactions'),
    path('transactions',views.transactions,name='transactions'),
    path('customers',views.customers,name='customers'),
    path('current_stock_price',views.current_stock_price,),
    path('buy_stocks',views.buy_stocks,name='buy_stocks'),
    path('sell_stocks',views.sell_stocks,name='sell_stocks'),
    path('stock_prices',views.stock_prices)
]