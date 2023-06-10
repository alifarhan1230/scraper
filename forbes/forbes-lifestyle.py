"""
    Speed scraping Forbes depends on your internet speed and computer resources where you're running this code. 
    Please be patient and wait, as this code will scrape all the news in detail.
    Remember!!! Do not close the browser while this code is running.
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
import time
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
    url = "https://www.forbes.com/lifestyle/?sh=733fef5e22d1"
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
    button_more_articles = driver.find_element(By.XPATH, '//*[@id="row-2"]/div/div/div[2]/div[31]/button')
    for _ in range(10):
        button_more_articles.click()
        print("Load More Articles....")
        time.sleep(2)
    



# Set URL of the webpage
def get_link_lifestyle():
    try:

        initialize_driver()
            
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        #print(soup)
        root_item = soup.find('div', class_='COe59', attrs={'data-test-e2e': 'stream articles'})
        cards = root_item.find_all('div', class_='NJl37fev')
        print("Number card:", len(cards))
        data_list = []
        for index, item in enumerate(cards):
            try:
                get_date = item.find('div', class_='ptbNeM0K')
                post_date = get_date.get_text()
            except AttributeError:
                title = None
                
            try:
                get_journalist = item.find('div', class_='-GPe57GX Q5lCM4EP xeEyB3Bw')
                journalist = get_journalist.get_text()
            except AttributeError:
                title = None
            
            try:
                get_title = item.find('h3', class_='EKqpiIkt')
                title = get_title.get_text()
            except AttributeError:
                title = None

            try:      
                get_headline = item.find('p', class_='A7hAxSNa')
                headline = get_headline.get_text()
            except AttributeError:
                title = None
            
            try:
                get_link = item.find('a', class_='_5ncu0TWl')
                link = get_link['href']
            except AttributeError:
                title = None
            
            try:
                get_image = item.find('img', class_='-bbwb19P')
                image = get_image['src']
            except AttributeError:
                title = None

            data_list.append({"post_date":post_date, 'journalist':journalist,'title_news':title, 'headline':headline, 'link': link, 'images':image})
            print(f'data: {index}')

        return data_list; #return data
    except Exception as e:
        print("An error occurred:", str(e))
    
    
    
def lifestyle():
    init_data = get_link_lifestyle()
    print(init_data)
    for index, data in enumerate(init_data):
        news_url = data['link']
        driver.get(news_url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        element = soup.find('div', class_='article-body')

        full_news_list = []

        if element is not None:
            p_tags = element.find_all('p')
            for p_tag in p_tags:
                full_news = p_tag.get_text()
                full_news_list.append(full_news)

        data['full_news'] = full_news_list
        print(f"{index}. pull data news in link: {news_url}")



    df = pd.DataFrame(init_data)
    column_order = ['post_date', 'journalist', 'title_news', 'headline', 'link', 'images', 'full_news']
    df = df[column_order]
    df.to_csv('csv/forbes_lifestyle.csv', index=False)


lifestyle()

