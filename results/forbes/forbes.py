import csv
import requests
from bs4 import BeautifulSoup


def forbes_real_estate():
    base_url = 'https://www.forbes.com/commercial-real-estate/?sh=173524e9719e';
        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('div', 'COe59')
    items = main_element.find_all('div')
    datas =[]
    for item in items:
        try: title = item.find('div', 'NJl37fev').text.strip()
        except: title=''
        
        datas.append([title])

  
    header_csv = ['News']
    writer = csv.writer(open('csv/forbes_real_estate.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
    
    
def forbes_life_style():
    base_url = 'https://www.forbes.com/arts/?sh=689235031b64';
        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('div', 'COe59')
    items = main_element.find_all('div')
    datas =[]
    for item in items:
        try: title = item.find('div', 'NJl37fev').text.strip()
        except: title=''        
        datas.append([title])

  
    header_csv = ['News']
    writer = csv.writer(open('csv/forbes_live_style.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
    
def forbes_money_banking():
    base_url = 'https://www.forbes.com/banking-insurance/?sh=27c79e763736';
        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('div', 'COe59')
    items = main_element.find_all('div')
    datas =[]
    for item in items:
        try: title = item.find('div', 'NJl37fev').text.strip()
        except: title=''
        
        datas.append([title])

  
    header_csv = ['News']
    writer = csv.writer(open('csv/forbes_money_banking.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
    
    
def forbes_investing():
    base_url = 'https://www.forbes.com/investing/?sh=611ad19d10ba';
        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('div', 'COe59')
    items = main_element.find_all('div')
    datas =[]
    for item in items:
        try: title = item.find('div', 'NJl37fev').text.strip()
        except: title=''
        
        datas.append([title])

  
    header_csv = ['News']
    writer = csv.writer(open('csv/forbes_investing.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
    
def forbes_taxes():
    base_url = 'https://www.forbes.com/taxes/?sh=7c3cf5702317';
        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('div', 'COe59')
    items = main_element.find_all('div')
    datas =[]
    for item in items:
        try: title = item.find('div', 'NJl37fev').text.strip()
        except: title=''
        
        datas.append([title])

  
    header_csv = ['News']
    writer = csv.writer(open('csv/forbes_taxes.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
    
    
    
          
forbes_real_estate()
forbes_life_style()
forbes_money_banking()
forbes_investing()
forbes_taxes()
