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
# set threshold
threshold = 440

while True:
    response = requests.get(url2)
    response_dict = json.loads(response.text)
    xrp_current_usd_value = response_dict['USD']

    # add value to history
    history.append(float(xrp_current_usd_value))
    print history

    # alert via message if XRP below set threshold
    if xrp_current_usd_value < threshold:
        my_message = 'ALERT: \n ETH is currently below $'
        my_message += str(threshold)
        my_message += '\n at $'
        my_message += str(xrp_current_usd_value)
        my_message += ' USD!'
        sendMessage(my_number, my_message)

    # send average of past 60 min ETH value
    if len(history) % 60 == 0:
        # send history average
        average_price = 'Average value for '
        average_price += 'past 60 min: $'
        average_price += str(np.mean(xrp_history[-60:]))
        sendMessage(my_number, average_price)

    # sleep a minute
    time.sleep(60)
