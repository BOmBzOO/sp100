from iexfinance.stocks import Stock
import os

os.environ['IEX_TOKEN'] = 'sk_33d0f37bacbb40aea6488085428bdee5'


a = Stock("AAPL")
print(a.get_quote())

tsla = Stock('TSLA')
print(tsla.get_price())
