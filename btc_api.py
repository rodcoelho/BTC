import sys
import requests
#(final step) from sendmessages import sendtext

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
#The relevant data is scraped from CoinDesk API - 'Powered by CoinDesk'
#CoinDesk website: https://www.coindesk.com/price/

BTC_price_list = []
#list used to store recent price points

def check_list_len():
    #checks length of list, if there are more than 12 data points, it will throw out old data
    if len(BTC_price_list) > 12:
        BTC_price_list[:] = BTC_price_list[:2]

def extractAndSaveBTC():
    #uses requests to pull data from CoinDesk, returns Bitcoin price (USD)
    BTCinfo = requests.get(url).json()
    return BTCinfo['bpi']['USD']['rate_float']

def add_new_price_to_list():
    #adds new data point to front of list
    x = extractAndSaveBTC()
    BTC_price_list.insert(0,x)

def check_price_delta():
    #simple price change formula
    delta = (BTC_price_list[0] - BTC_price_list[1]) / (BTC_price_list[1])
    return delta

def main():
    #main function, not yet finished
    check_list_len()
    add_new_price_to_list()
    if len(BTC_price_list) > 1:
        recent_delta = check_price_delta()

if __name__ == "__main__":
    main()

