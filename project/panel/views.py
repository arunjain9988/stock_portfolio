# from django.shortcuts import render,HttpResponse,get_object_or_404
# from .models import Stock
# import requests,json
# from datetime import datetime
# from django.http import JsonResponse

# # Create your views here.
# def dashboard(request):
#     return render(request,'dashboard.html',{
#         'name':'arun'
#     })

# def transactions(request):
#     return render(request,'transactions.html')

# def customers(request):
#     return render(request,'customers.html')

# def current_stock_price(request):
#     stock = get_object_or_404(Stock,pk=request.POST.get('symbol'))
#     return HttpResponse(stock.current_price)

# def buy_stocks(request):
#     return render(request,'buy_stocks.html')

# def stock_prices(request):   
#     if (request.GET):
#         url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + request.GET.get('symbol') + "&interval=5min&apikey=OA8OLUQDR9KVARZH"
#         response = requests.get(url)
#         js = response.text
#         dct = json.loads(js)
#         print(dct)
#         # prices = []
#         tmp = []
#         price = dct['Time Series (5min)'].values()
#         timestamps = dct['Time Series (5min)'].keys()
#         tmptimes = []
#         for t in timestamps:
#             tmptimes.append(datetime.timestamp(datetime.strptime(t,"%Y-%m-%d %H:%M:%S")))
#         for p in price:
#             tmp.append(p['4. close'])
#         prices = {'prices':tmp,'timestamp':tmptimes}
#         print(prices)
#         return JsonResponse(prices,safe=False)

# def stock_prices_alternate(request):
#     if (request.GET):
#         url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"
#         querystring = {"interval":"1m","symbol":"GOOGL","range":"1d","region":"US"}

#         headers = {
#             'x-rapidapi-key': "4ab85a3d80msh46bfef8c1f00254p16160ejsnf9fe68537b2a",
#             'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
#             }

#         response = requests.request("GET", url, headers=headers, params=querystring)
#         print(response.text)
#         js = response.text
#         dct = json.loads(js)
#         prices = dct['chart']['result'][0]['indicators']['quote'][0]['close']
#         timestamp = dct['chart']['result'][0]['timestamp']
#         print(timestamp)
#         dct = {'prices':prices,'timestamp':timestamp}
#         # prices = []
#         # price = dct['Time Series (5min)'].values()
#         # for p in price:
#         #     prices.append(p['4. close'])
#         # print(prices)
#         return JsonResponse(dct,safe=False)
    



# # print(response.json())