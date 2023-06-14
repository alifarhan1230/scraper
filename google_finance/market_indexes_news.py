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
    url = "https://www.google.com/finance/markets/indexes?hl=en"
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

def market_indexes_news():
    initialize_driver()

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    root_item = soup.find('div', class_='Vd323d', attrs={'role': 'main'})                
    divs = root_item.find_all('div', class_='Sy70mc')
    for div in divs:
        ul = div.find('ul', class_='sbnBtf')
        if ul:
            lis = ul.find_all('li')
            for li in lis:
                anchor = li.find('a')
                if anchor:
                    link = anchor['href']
                    driver.execute_script("window.open(arguments[0], '_blank');", link)
                    driver.switch_to.window(driver.window_handles[-1])
                    new_tab_url = driver.current_url
                    driver.get(new_tab_url)

                    new_tab_content = driver.page_source
                    new_tab_soup = BeautifulSoup(new_tab_content, 'html.parser')
                    main_content = new_tab_soup.find('main')
                    
                    if main_content:
                        cards = main_content.find_all('div', class_='qQfHId')
                        if cards:
                            for card in cards:
                                news = card.find_all('div', class_=['zLrlHb'])
                                if news:
                                    for item in news:
                                        try:
                                            news_title = item.find('div', class_='F2KAFc')
                                            title = news_title.get_text()
                                           
                                        except AttributeError:
                                            title = None
                                            
                                        try:
                                            link_tag = item.find('a')
                                            if link_tag:
                                                link = link_tag['href']
                                                
                                            else:
                                                link = None
                                        except AttributeError:
                                            link = None
                                            
                                        data_list.append({"market":new_tab_url, "title_news": title, "link_news":link})
                                        print(f'success pull data market news from google finance...')
                                            
                                        
                    time.sleep(5)
                    driver.close()
                    # Switch back to the original tab
                    driver.switch_to.window(driver.window_handles[0])

    df = pd.DataFrame(data_list)
    column_order = ['market', 'title_news', 'link_news']
    df = df.reindex(columns=column_order)
    df.to_csv('csv/market_indexes_news.csv', mode='a', index=False)
    
market_indexes_news()



    
    


