"""
    Speed scraping google finance depends on your internet speed and computer resources where you're running this code. 
    Please be patient and wait, as this code will scrape all the news in detail.
    Remember!!! Do not close the browser while this code is running..
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, os
import pandas as pd
import requests

# Configure Chrome options
chrome_options = Options()
webdriver_service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
   
for key, value in headers.items():
    chrome_options.add_argument(f"--header={key}:{value}")
    
def initialize_driver():
    url = "https://www.google.com/finance/?hl=en"
    try:
        driver.get(url)
        response_code = requests.head(url).status_code
        if response_code == 200:
            print("Request was successful")
        else:
            print(f"Request failed with status code: {response_code}")
    except Exception as e:
        print("Failed to make the request:", str(e))
    print('Starting Driver...')
 
data_list = [] #news list    
def loop_tab_news(cards):
    data=[]
    for index, item in enumerate(cards):
        try:
            get_resource_news = item.find('div', class_="sfyJob")
            resource = get_resource_news.get_text()
            
        except AttributeError:
            resource = None
            
        try:
            get_time = item.find('div', class_='Adak')
            time = get_time.get_text()
            
        except AttributeError:
            time = None
            
        try:
            get_title = item.find('div', class_='Yfwt5')
            title = get_title.get_text()
            
        except AttributeError:
            title = None
            
        try:
            get_link = item.find('div', class_='z4rs2b')
            link_tag = get_link.find('a')
            if link_tag:
                link = link_tag['href']
                
            else:
                link = None
        except AttributeError:
            link = None
            
        data.append({"news_resource":resource, 'news_time':time,'news_title':title, 'news_link':link,})
        print(f'data: {index}')
    return data
    

def today_financial_news():
    
    initialize_driver()
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    root_item = soup.find('section', attrs={'aria-labelledby': 'news-title'})
    top_stories = root_item.find_all('div', class_='yY3Lee', attrs={'jscontroller': 'ZpnVYd'})
    res_top_stories = loop_tab_news(top_stories)
    data_list.append(res_top_stories)
    
    local_markets = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[4]/div/div/div[1]/c-wiz[2]/section/div[2]/div/div[1]/div/div/div/div/div[2]')
    local_markets.click()
    time.sleep(3)
    local_market = root_item.find_all('div', class_='yY3Lee', attrs={'jscontroller': 'ZpnVYd'})
    res_local_market = loop_tab_news(local_market)
    data_list.append(res_local_market)
    
    world_markets = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[4]/div/div/div[1]/c-wiz[2]/section/div[2]/div/div[1]/div/div/div/div/div[3]')
    world_markets.click()
    time.sleep(3)
    worlds_markets_cards = root_item.find_all('div', class_='yY3Lee', attrs={'jscontroller': 'ZpnVYd'})
    res_worlds_markets_cards = loop_tab_news(worlds_markets_cards)
    data_list.append(res_worlds_markets_cards)
    
    data = [item for sublist in data_list for item in sublist]
    df = pd.DataFrame(data)
    column_order = ['news_resource', 'news_time', 'news_title', 'news_link']
    df = df.reindex(columns=column_order)
    df.to_csv('csv/google_finance_news.csv', mode='a', index=False)

    
today_financial_news()

    
    


