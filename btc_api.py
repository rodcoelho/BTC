import sys, time
import requests
#(final step) from sendmessages import sendtext

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
#The relevant data is scraped from CoinDesk API - 'Powered by CoinDesk'
#CoinDesk website: https://www.coindesk.com/price/

# temporary solution: sys.argv[1] will be the time interval - or how often - the user will want to check
time_interval = (float(sys.argv[1]) * 60 *60)

def get_latest_BTC():
    #uses requests to pull data from CoinDesk, returns Bitcoin price (USD)
    BTCinfo = requests.get(url).json()
    return BTCinfo['bpi']['USD']['rate_float']

def check_price_delta(latestBTC, oldBTC):
    x = (latestBTC - oldBTC) / (oldBTC)
    if x != 0 or x != None:
        return x*100
    else:
        return 'zero change - or more likely, there is an error'

def main():
    latestBTC = get_latest_BTC()
    time.sleep(time_interval) #need to take this out and use cron tabs
                                #first, need to find way to store data points outside of .py file
    oldBTC = latestBTC
    latestBTC = get_latest_BTC()
    delta = check_price_delta(latestBTC,oldBTC)
    print('{}'.format(delta))

if __name__ == "__main__":
    main()

