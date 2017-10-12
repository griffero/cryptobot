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


def display_eth_info(currencies_name):
    with open(currencies_path + currencies_name) as data_file:
           # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
           data = json.load(data_file)
           market_name = data['market_name']
           currencies = data['currencies']
           if currencies == "ETH-CLP":
               max_bid =  format_currency(data['max_bid'], 'CLP', locale='es_CL')
               min_ask =  format_currency(data['min_ask'], 'CLP', locale='es_CL')
               last_price =  format_currency(data['last_price'], 'CLP', locale='es_CL')
           else:
               max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
               min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
               last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
           last_update = data['last_update']
           #data['min_ask'] = Money(data['max_bid'], 'CLP')
           #data['last_price'] = Money(data['max_bid'], 'CLP')
           return '\n' + "%s %s:\n  - max bid: %s\n  - min ask: %s\n  - last price: %s\n  - Last Update: %s" % (market_name, currencies, max_bid, min_ask, last_price, last_update)

def send_ethclp_stats():
    out = ""
    out += display_eth_info('eth_clp.json')
    out += display_eth_info('eth_clp_cryptomkt.json')
    out += display_eth_info('bitstamp_eth_usd.json')
    bot.sendMessage(group, out)

def send_btcclp_stats():
             out = ""
             with open(currencies_path + 'btc_clp.json') as data_file:
                    # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'CLP', locale='es_CL')
                    min_ask =  format_currency(data['min_ask'], 'CLP', locale='es_CL')
                    last_price =  format_currency(data['last_price'], 'CLP', locale='es_CL')
                    last_update = data['last_update']
                    #data['min_ask'] = Money(data['max_bid'], 'CLP')
                    #data['last_price'] = Money(data['max_bid'], 'CLP')
                    out += '\n' + "SURBTC (BTC-CLP):\n  - max bid: %s\n  - min ask: %s\n  - last price: %s\n  - Last Update: %s" % (max_bid, min_ask, last_price, last_update)

             with open(currencies_path + 'bitstamp_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
                    min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
                    last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
                    last_update = data['last_update']

                    out += '\n' + "Bitstamp (BTC-USD):\n  - max bid: %s\n  - min ask: %s\n  - last price: %s\n  - Last Update: %s" % (max_bid, min_ask, last_price, last_update)
             bot.sendMessage(group, out)

def forcerefresh():
             os.system("python /root/cryptobot/update_scripts/surbtc.py")
             bot.sendMessage(group, "Valores SURBTC Actualizados")
             os.system("python /root/cryptobot/update_scripts/cryptomkt.py")
             bot.sendMessage(group, "Valores Crytomkt Actualizados")
             os.system("python /root/cryptobot/update_scripts/bitstamp.py")
             bot.sendMessage(group, "Valores Bitstamp Actualizados")

             send_ethclp_stats()
             send_btcclp_stats()

def arbitraje(btc=1, eth=1):
             out = "Oportunidades de Arbitraje: "
             usd_clp_rate = ""
             with open(currencies_path + 'usd_clp.json') as data_file:
                   data = json.load(data_file)
                   usd_clp_rate = float(data['last_rate'])
             print usd_clp_rate
             ### BITCOIN
             surbtc_btc_max_bid = ""
             surbtc_btc_min_ask = ""
             surbtc_btc_last_price = ""
             bitstamp_btc_max_bid = ""
             bitstamp_btc_min_ask = ""
             bitstamp_btc_last_price = ""

             with open(currencies_path + 'btc_clp.json') as data_file:
                    # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                    data = json.load(data_file)
                    surbtc_btc_max_bid =  float(data['max_bid'])
                    surbtc_btc_min_ask =  float(data['min_ask'])
                    surbtc_btc_last_price = float(data['last_price'])
                    #data['min_ask'] = Money(data['max_bid'], 'CLP')
                    #data['last_price'] = Money(data['max_bid'], 'CLP')

             with open(currencies_path + 'bitstamp_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    bitstamp_btc_max_bid =  float(data['max_bid'])
                    bitstamp_btc_min_ask =  float(data['min_ask'])
                    bitstamp_btc_last_price =  float(data['last_price'])
             # Detectar diferencia de ultim precio
             if bitstamp_btc_last_price*usd_clp_rate > surbtc_btc_last_price:
                    maxbtc = format_currency(int(bitstamp_btc_last_price*btc*usd_clp_rate), 'CLP', locale='es_CL')
                    minbtc = format_currency(int(surbtc_btc_last_price*btc), 'CLP', locale='es_CL')
                    margin = format_currency(int(bitstamp_btc_last_price*btc*usd_clp_rate)-int(surbtc_btc_last_price*btc), 'CLP', locale='es_CL')
                    out +=  "\n" + "  - Al comprar %s BTC en SurBTC a %s, podria venderse en BitStamp a %s y ganar %s" % (btc, minbtc, maxbtc, margin)
             if bitstamp_btc_last_price*usd_clp_rate < surbtc_btc_last_price:
                    maxbtc = format_currency(int(surbtc_btc_last_price*btc), 'CLP', locale='es_CL')
                    minbtc = format_currency(int(bitstamp_btc_last_price*btc*usd_clp_rate), 'CLP', locale='es_CL')
                    margin = format_currency(int(surbtc_btc_last_price*btc-bitstamp_btc_last_price*btc*usd_clp_rate), 'CLP', locale='es_CL')
                    out += "\n" + "  - Al comprar %s BTC en Bitstamp a %s, podria venderse en SurBTC a %s y ganar %s" % (btc, minbtc, maxbtc, margin)


             ### ETH
             surbtc_eth_max_bid = ""
             surbtc_eth_min_ask = ""
             surbtc_eth_last_price = ""
             cryptomkt_eth_max_bid = ""
             cryptomkt_eth_min_ask = ""
             cryptomkt_eth_last_price = ""
             bitstamp_eth_max_bid = ""
             bitstamp_eth_min_ask = ""
             bitstamp_eth_last_price = ""

             with open(currencies_path + 'eth_clp.json') as data_file:
                    # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                    data = json.load(data_file)
                    surbtc_eth_max_bid =  float(data['max_bid'])
                    surbtc_eth_min_ask =  float(data['min_ask'])
                    surbtc_eth_last_price = float(data['last_price'])
                    #data['min_ask'] = Money(data['max_bid'], 'CLP')
                    #data['last_price'] = Money(data['max_bid'], 'CLP')

            with open(currencies_path + 'eth_clp_cryptomkt.json') as data_file:
                   # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                   data = json.load(data_file)
                   cryptomkt_eth_max_bid =  float(data['max_bid'])
                   cryptomkt_eth_min_ask =  float(data['min_ask'])
                   cryptomkt_eth_last_price = float(data['last_price'])
                   #data['min_ask'] = Money(data['max_bid'], 'CLP')
                   #data['last_price'] = Money(data['max_bid'], 'CLP')

             with open(currencies_path + 'bitstamp_eth_usd.json') as data_file:
                    data = json.load(data_file)
                    bitstamp_eth_max_bid =  float(data['max_bid'])
                    bitstamp_eth_min_ask =  float(data['min_ask'])
                    bitstamp_eth_last_price =  float(data['last_price'])
             # Detectar diferencia de ultim precio
             if bitstamp_eth_last_price*usd_clp_rate > surbtc_eth_last_price:
#                    print "Existe una oportunidad de comprar eth barato en SurBTC y venderlo mas caro en Bitstamp"
                    maxeth = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                    mineth = format_currency(int(surbtc_eth_last_price*eth), 'CLP', locale='es_CL')
                    margin = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate)-int(surbtc_eth_last_price*eth), 'CLP', locale='es_CL')
                    out += '\n' + "  - Al comprar %s ETH en SurBTC a %s, podria venderse en BitStamp a %s y ganar %s" % (eth, mineth, maxeth, margin)
             if bitstamp_eth_last_price*usd_clp_rate < surbtc_eth_last_price:
#                    print "Existe una oportunidad de comprar eth barato en Bitstamp y venderlo mas caro en SurBTC"
                    maxeth = format_currency(int(cryptomkt_eth_last_price*eth), 'CLP', locale='es_CL')
                    mineth = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                    margin = format_currency(int(cryptomkt_eth_last_price*eth-bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                    out += '\n' + "  - Al comprar %s ETH en Bitstamp a %s, podria venderse en SurBTC a %s y ganar %s" % (eth, mineth, maxeth, margin)
            if bitstamp_eth_last_price*usd_clp_rate > cryptomkt_eth_last_price:
            #                    print "Existe una oportunidad de comprar eth barato en SurBTC y venderlo mas caro en Bitstamp"
                   maxeth = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                   mineth = format_currency(int(surbtc_eth_last_price*eth), 'CLP', locale='es_CL')
                   margin = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate)-int(surbtc_eth_last_price*eth), 'CLP', locale='es_CL')
                   out += '\n' + "  - Al comprar %s ETH en Crytomkt a %s, podria venderse en BitStamp a %s y ganar %s" % (eth, mineth, maxeth, margin)
            if bitstamp_eth_last_price*usd_clp_rate < cryptomkt_eth_last_price:
            #                    print "Existe una oportunidad de comprar eth barato en Bitstamp y venderlo mas caro en SurBTC"
                   maxeth = format_currency(int(cryptomkt_eth_last_price*eth), 'CLP', locale='es_CL')
                   mineth = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                   margin = format_currency(int(cryptomkt_eth_last_price*eth-bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                   out += '\n' + "  - Al comprar %s ETH en Bitstamp a %s, podria venderse en Crytomkt a %s y ganar %s" % (eth, mineth, maxeth, margin)


             out += '\n\n' + "Tasa de cambio: 1 USD = %s CLP (Yahoo Finance)" % (usd_clp_rate)
             out += '\n' + 'WIP: Incluir costos de transacciones en calculo'
             #print out
             bot.sendMessage(group, out)


def handle(msg):
   content_type, chat_type, chat_id = telepot.glance(msg)
   print content_type
   print chat_type
   print chat_id
   if content_type.strip() == 'text' and chat_type.strip() == 'group' and str(chat_id) == '-268121898':
         if "/eth" == msg["text"]:
             send_ethclp_stats()
             return
         if "/btc" == msg["text"]:
             send_btcclp_stats()
             return
         if "/forcerefresh" == msg["text"]:
             forcerefresh()
             return
         if "/arbitraje" in msg["text"]:
             if "/arbitraje" == msg["text"]:
                arbitraje()
             if len(msg["text"].split(" ")) == 3:
                cmd, btc, eth = msg["text"].split(" ")
                arbitraje(float(btc), float(eth))
             return
         print msg["text"]
         print msg["date"]


bot.message_loop(handle)

while 1:
   time.sleep(10)
