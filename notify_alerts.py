import telepot
import time
import os
import json
from moneyed import Money, CLP
from moneyed.localization import format_money
from decimal import Decimal
from babel.numbers import format_currency

from locale import *
import locale
setlocale(LC_NUMERIC, 'es_CL.UTF-8')
setlocale(LC_ALL, 'es_CL.UTF-8')
setlocale(LC_MONETARY, 'es_CL.UTF-8')


bot = telepot.Bot('331003353:AAEy6xrXZ-uIRJmq4q-jNVtoe0RjzXlzBSU')
group = '-268121898'

currencies_path = '/root/cryptobot/currencies/'


def getmarkets():
   currencyfiles = []
   markets = {}
   for path, directories, files in os.walk(currencies_path):
     for file in files:
        if ".json" in file:
          currencyfiles.append(file)
   for currencyfile in currencyfiles:
       with open('/root/cryptobot/currencies/' + currencyfile) as data_file:
          data = json.load(data_file)
          if "currencies" in data:
             currency = {}
             currency[data['currencies']] = {}
             currency[data['currencies']]['last_price'] = data['last_price']
             currency[data['currencies']]['max_bid'] = data['max_bid']
             currency[data['currencies']]['min_ask'] = data['min_ask']
             if data['market_name'] not in markets:
                markets[data['market_name']] = []
                markets[data['market_name']].append(currency)
             else:
                markets[data['market_name']].append(currency)

   return markets

def getalerts():
   alertfiles = []
   alerts = {}
   for path, directories, files in os.walk('/root/cryptobot/alerts/'):
     for file in files:
        if ".json" in file:
          alertfiles.append(file)
   for alertfile in alertfiles:
       with open('/root/cryptobot/alerts/' + alertfile) as data_file:
          data = json.load(data_file)
          alerts[alertfile] = {}
          alerts[alertfile]['currency'] = data['currency']
          alerts[alertfile]['limit']    = data['limit']
          alerts[alertfile]['if']       = data['if']
   return alerts


alerts_list = []
alerts_dict = getalerts()
for alert in alerts_dict:
  alerts_dict[alert]['name'] = alert
  alerts_list.append(alerts_dict[alert])
  
markets = getmarkets()

for market in markets:
  for currencies in markets[market]:
     for currency in currencies:
       for alert in alerts_list:
         if currency == alert['currency']:
           # print "%s tiene la currency %s del alert %s" % (market, currency, alert['name'])
           if alert['if'] == "upper":
              if float(alert['limit']) <= currencies[currency]['last_price']:
                msg_out = "*Alerta %s*: El valor de %s en %s es mayor a %s (valor actual: %s)" % (alert['name'], alert['currency'], market, alert['limit'], currencies[currency]['last_price'])
                bot.sendMessage(group, msg_out, parse_mode="markdown")
           if alert['if'] == "lower":
              if float(alert['limit']) >= currencies[currency]['last_price']:
                msg_out = "*Alerta %s*: El valor de %s en %s es menor a %s (valor actual: %s)" % (alert['name'], alert['currency'], market, alert['limit'], currencies[currency]['last_price'])
                bot.sendMessage(group, msg_out, parse_mode="markdown")
      
  
