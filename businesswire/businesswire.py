import csv
import requests
from bs4 import BeautifulSoup


def businesswire_news_industry():
    query_params = 'vnsId=31209'
    base_url = 'https://www.businesswire.com/portal/site/home/news/industry/?{}'.format(query_params)
    

        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('ul', 'bwNewsList')
    items = main_element.find_all('li')
    datas =[]
    for item in items:
        try: title = item.find('span', {'itemprop':'headline'}).text.strip()
        except: title=None
        datas.append([title])

  
    header_csv = ['News']
    writer = csv.writer(open('csv/businesswire_news_industry.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
    

businesswire_news_industry()
