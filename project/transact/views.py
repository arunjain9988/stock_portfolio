from django import http
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from .models import Customer, Stock, Transaction
import requests,json
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.

def login(request):
    if (request.POST):
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = auth.authenticate(username=email, password=password)
        request.session.set_expiry(30*60)
        request.session.__setitem__('_requests',0)
        if user is not None:
            auth.login(request, user)
            if user.groups.all().count() == 0:
                group = Group.objects.get_or_create(name='users')[0]
                # permissions_list = Permission.objects.all()
                # group.permissions.set(permissions_list)
                user.groups.add(group)
            messages.success(request,'Login Successful')
            return redirect('/')
        else:
            messages.error(request, "Username or password is incorrect")
            return render(request, 'login.html')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if (request.POST):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(fname,lname,email,password)
        try:
            print(email)
            user = User.objects.get(username=email)
            messages.error(request,'Username already registered')
        except:
            # password validation
            if password == '':
                messages.error(request,'Password cannot be empty')
            else:
                user = User.objects.create_user(username=email,password=password,email=email,first_name=fname,last_name=lname)
                group = Group.objects.get_or_create(name = 'users')[0]
                user.groups.add(group)
                user = auth.authenticate(username=email, password=password)
                request.session.set_expiry(30*60)
                request.session.__setitem__('_requests',0)
                auth.login(request, user)
                messages.success(request,'User Created Successfully')
        return redirect('/')
    return render(request,'register.html')

def forgot_password(request):
    return render(request,'forget_pass.html')

# @login_required(redirect_field_name='login',login_url='login')
def dashboard(request):
    return render(request,'dashboard.html',{
        'name':'arun'
    })

@login_required(login_url='/login',redirect_field_name='/')
def transactions(request):
    return render(request,'transactions.html',{
        'transactions':Transaction.objects.all()
    })

def customers(request):
    if (request.POST):
        return HttpResponse('200')
    return render(request,'customers.html',{
        'customers':Customer.objects.all()
    })

def current_stock_price(request):
    stock = get_object_or_404(Stock,pk=request.POST.get('symbol'))
    return HttpResponse(stock.current_price)

def buy_stocks(request):
    return render(request,'buy.html',{
        'customers':Customer.objects.all(),
        'stocks':Stock.objects.all()
    })

def sell_stocks(request):
    return render(request,'sell.html',{
        'customers':Customer.objects.all(),
        'stocks':Stock.objects.all()
    })

def stock_prices(request):   
    if (request.GET):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + request.GET.get('symbol') + "&interval=5min&apikey=OA8OLUQDR9KVARZH"
        response = requests.get(url)
        js = response.text
        dct = json.loads(js)
        print(dct)
        # prices = []
        tmp = []
        price = dct['Time Series (5min)'].values()
        timestamps = dct['Time Series (5min)'].keys()
        tmptimes = []
        for t in timestamps:
            tmptimes.append(datetime.timestamp(datetime.strptime(t,"%Y-%m-%d %H:%M:%S")))
        for p in price:
            tmp.append(p['4. close'])
        prices = {'prices':tmp,'timestamp':tmptimes}
        print(prices)
        return JsonResponse(prices,safe=False)

def stock_prices_alternate(request):
    if (request.GET):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"
        querystring = {"interval":"1m","symbol":"GOOGL","range":"1d","region":"US"}

        headers = {
            'x-rapidapi-key': "4ab85a3d80msh46bfef8c1f00254p16160ejsnf9fe68537b2a",
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        js = response.text
        dct = json.loads(js)
        prices = dct['chart']['result'][0]['indicators']['quote'][0]['close']
        timestamp = dct['chart']['result'][0]['timestamp']
        print(timestamp)
        dct = {'prices':prices,'timestamp':timestamp}
        # prices = []
        # price = dct['Time Series (5min)'].values()
        # for p in price:
        #     prices.append(p['4. close'])
        # print(prices)
        return JsonResponse(dct,safe=False)
    



# print(response.json())