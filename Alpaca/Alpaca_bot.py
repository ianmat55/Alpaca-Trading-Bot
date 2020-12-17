import alpaca_trade_api as alpaca
import requests, json, pprint
from key import *

endpoint_url = 'https://paper-api.alpaca.markets'
account = '{}/v2/account'.format(endpoint_url)
orders = '{}/v2/orders'.format(endpoint_url) 
HEADERS = {'APCA-API-KEY-ID':key, 'APCA-API-SECRET-KEY':secret}

def get_account():
	r = requests.get(account, headers=HEADERS)
	
	return json.loads(r.content)



class Order():
	
	def __init__(self, symbol, qty, side, type, time_in_force):
		
		self.symbol = symbol
		self.qty = qty
		self.side = side
		self.type = type
		self.time_in_force = time_in_force
		
		
		
	def place_order(self):
		
		data = {
			"symbol": self.symbol,
			"qty": self.qty,
			"side": self.side,
			"type": self.type,
			"time_in_force": self.time_in_force
		}
		
		r = requests.post(orders, json=data, headers=HEADERS)
		
		pprint.pprint(json.loads(r.content))
		
		return ''

buy_AAPL = Order('AAPL', 2, 'buy', 'market', 'gtc')
buy_AAPL.place_order()


		
	
		
		





    
