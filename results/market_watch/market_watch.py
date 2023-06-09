import csv
import requests
from bs4 import BeautifulSoup


def news_market():

    base_url = 'https://www.marketwatch.com/markets/us?mod=side_nav'
    

        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('div', 'collection__elements j-scrollElement')
    items = main_element.find_all('div', class_='element element--article no-image MarketWatchcom')

    
    datas = []
    for item in items:
        title = item.find('p', 'article__summary').text.strip()
        print(f"store data into csv")
        datas.append([title])
        
    items1 = main_element.find_all('div', class_="element element--article MarketWatchcom")
    for item in items1:
        title = item.find('p', 'article__summary').text.strip()
        datas.append([title])
        print(f"store data into csv")
  
    header_csv = ['News']
    writer = csv.writer(open('csv/market_news.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
      
#calls
news_market()
