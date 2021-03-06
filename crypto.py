from twilio.rest import Client
from urllib.request import urlopen
from bs4 import BeautifulSoup
from keys import accountSID, authToken

client = Client(accountSID, authToken)
TwilioNumber = '+14126681320'
mycellphone = '+18325097076'

webpage = 'https://coinmarketcap.com/'

page = urlopen(webpage)			
soup = BeautifulSoup(page, 'html.parser')

title = soup.title

bitcoin_table = soup.find('table')
rows = bitcoin_table.findAll('tr')

for x in range (1,6):
    cols = rows[x].findAll('td')
    rank = x
    name = cols[1].text
    current_price = cols[2].text.replace(',', '').replace('$','')
    current_price = float(current_price)
    percent_change = cols[3].text
    change_float = float(percent_change.text.strip('%'))
    old_price = round(current_price / (1+ (change_float/100)), 2)

    print(f"Rank : {rank}")
    print(f"Name: {name}")
    print(f"Current Price: {current_price}")
    print(f"Old Price: {old_price}")
    print(f"% Change in last 24 hours: {percent_change}")
  

    if name == "Bitcoin":
        btc = current_price
        if btc < 40000:
            textmessage = client.messages.create(to= mycellphone, from_= TwilioNumber, body ='BTC fell below $40,000')
    if name == "Ethereum":
        eth = current_price
        if eth < 3000:
            textmessage = client.messages.create(to= mycellphone, from_= TwilioNumber, body ='ETH fell below $3,000')
 
    input()
