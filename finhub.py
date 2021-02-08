# #https://pypi.org/project/websocket_client/
# import websocket

# def on_message(ws, message):
#     print(message)

# def on_error(ws, error):
#     print(error)

# def on_close(ws):
#     print("### closed ###")

# def on_open(ws):
#     ws.send('{"type":"subscribe","symbol":"IBM"}')
#     ws.send('{"type":"subscribe","symbol":"AMZN"}')
#     # ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
#     ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c0fitrv48v6snribcau0",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()

# import requests

# Register new webhook for earnings
# r = requests.post('https://finnhub.io/api/v1/webhook/add?token=c0fitrv48v6snribcau0', json={'event': 'earnings', 'symbol': 'AAPL'})
# res = r.json()
# print(res)

# webhook_id = res['id']
# # List webhook
# r = requests.get('https://finnhub.io/api/v1/webhook/list?token=c0fitrv48v6snribcau0')
# res = r.json()
# print(res)

r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=c0fitrv48v6snribcau0')
print(r.json())