import json
import requests
import time
import numpy as np
from datetime import datetime
from message import sendMessage


my_number = raw_input('Enter phone #: ')

# cryptocompare API
# get XRP values (USD, EUR)
url2 = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR'
# get coin list
url3 = 'https://www.cryptocompare.com/api/data/coinlist/'

# saves value of XRP at given time, list of tuples
history = []

def getPriceAverage():
    return np.mean(history)

# set threshold
threshold = 455

while True:
    response = requests.get(url2)
    response_dict = json.loads(response.text)
    xrp_current_usd_value = response_dict['USD']

    # add value to history
    xrp_history.append(float(xrp_current_usd_value))
    print history

    # alert via message if XRP below set threshold
    if xrp_current_usd_value < threshold:
        my_message = 'ALERT \n'
        my_message += 'ETH is currently below $440 \n'
        my_message += 'at $'
        my_message += str(xrp_current_usd_value)
        my_message += ' USD!'
        sendMessage(my_number, my_message)

    # send an average of past 10 min XRP value
    # if len(history) % 10 == 0:
    #     #print history
    #     average_price = 'Average value \n'
    #     average_price += 'past 10 min: $'
    #     average_price += str(np.mean(xrp_history[-10:]))
    #     sendMessage(my_number, average_price)

    time.sleep(60)
