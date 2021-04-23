from django.urls import path
from . import views

urlpatterns = [
    path('',views.transactions,name='transactions'),
    path('logout',views.logout,name='logout'),
    path('transactions',views.transactions,name='transactions'),
    path('customers',views.customers,name='customers'),
    path('current_stock_price',views.current_stock_price,),
    path('buy_stocks',views.buy_stocks,name='buy_stocks'),
    path('sell_stocks',views.sell_stocks,name='sell_stocks'),
    path('stock_prices',views.stock_prices),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('forgot_password',views.forgot_password,name='forgot_password')
]