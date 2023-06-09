"""
    this file will download all pdf files
    in this url https://www.bea.gov/data/gdp/gdp-industry
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pathlib

options = webdriver.ChromeOptions()
path = pathlib.Path().absolute()

def scrape_files_current_release():
    preferences = {
    'download.default_directory': f'{path}/current_release', 
    'safebrowsing.enabled':False,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    
    }

    options.add_experimental_option('prefs', preferences)

    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://www.bea.gov/data/gdp/gdp-industry')
        items = driver.find_elements(By.XPATH, "//ul[@class='list-group']/li")

        for index, item in enumerate(items):
            link = item.find_element(By.TAG_NAME, 'a')
            link.click()
            time.sleep(7)
            print(f"downloading files current release category: {index} ")
            
        driver.close()
        
    except Exception as e:
        print(f"cannot download files current release {e}")


def consumer_spending():
    preferences = {
    'download.default_directory': f'{path}/consumer_spending', 
    'safebrowsing.enabled':False,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    
    }

    options.add_experimental_option('prefs', preferences)

    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://www.bea.gov/data/consumer-spending/main')
        items = driver.find_elements(By.XPATH, '//*[@id="collapse1"]/ul')
        
    except Exception as e:
        print(f"cannot download files current release {e}")

def bea():
    print("====== scrape current release data industry =======")
    scrape_files_current_release()


bea()
