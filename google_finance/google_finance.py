import csv
import requests
from bs4 import BeautifulSoup


def google_finance_update_market():
    category = 'indexes';
    country = 'americas';
    base_url = 'https://www.google.com/finance/markets/{}/{}?hl=en'.format(category, country)
    
    #for page in range(1, 8):
        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('ul', 'sbnBtf')
    items = main_element.find_all('li')
    
    datas = []
    for item in items:
        type_market = item.find('div', 'COaKTb').text
        market_name = item.find('div', 'ZvmM7').text
        market_price = item.find('div','YMlKec').text
        try: market_update = item.find('span', 'P2Luy').text
        except: market_update= ''
        market_update_in_percen = item.find('div', 'JwB6zf').text
        datas.append([type_market, market_name, market_price, market_update, market_update_in_percen])    
        
    header_csv = ['Type Market', 'Market Name', 'Market Price', 'Market Update', 'Market Update in %']
    writer = csv.writer(open('csv/google_finance_update_market.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
          
#call
google_finance_update_market()
