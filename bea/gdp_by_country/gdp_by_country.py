"""
    this file will extract data in pdf file gdp / quartal
    page 1-2, 4-55
"""

import tabula
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os
import pathlib
import PyPDF2
import pandas as pd

options = webdriver.ChromeOptions()
path = pathlib.Path().absolute()

def scrape_files_current_release():
    preferences = {
    'download.default_directory': f'{path}', 
    'safebrowsing.enabled':False,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    
    }

    options.add_experimental_option('prefs', preferences)

    driver = webdriver.Chrome(options=options)

    try:
        file_name = ''
        driver.get('https://www.bea.gov/data/gdp/gdp-county-metro-and-other-areas')
        link = driver.find_element(By.XPATH, "//a[contains(text(), 'Full Release & County Tables')]")
        link.click()
        time.sleep(7)

        # Get the latest downloaded file
        latest_file = max(
            [f for f in os.listdir(f'{path}')],
            key=lambda x: os.path.getctime(os.path.join(f'{path}', x))
        )
        print(f"Downloaded file: {latest_file}")
        file_name = latest_file
        
        driver.close()
        return file_name

    except Exception as e:
        print(f"Cannot download files current release: {e}")
        

def extract_gdp_by_country():
    file_name = scrape_files_current_release()
    print('wait for extract data form pdf file....')
    # Provide the path to your PDF file
    pdf_file_path = f'{file_name}';
    page_number = "4-55"
    tables = tabula.read_pdf(pdf_file_path, pages=page_number)

    start_page = 4

    # Iterate over extracted tables
    for i, table in enumerate(tables):
        start_page +=1
        df = pd.DataFrame(table)

        # Save the DataFrame as a CSV file
        csv_file_path = f'table_{i+1}_page_{start_page}.csv'
        df.to_csv(csv_file_path, index=False)

        print(f"Table {i+1} from page {start_page} saved as {csv_file_path}")
        
    return file_name;



def real_gdp_by_industry(pdf_file, area):
    df = tabula.read_pdf(pdf_file, pages=1, area=area, multiple_tables=True)
    table_data = pd.concat(df)
    table_data = table_data.dropna(how='all', axis=0)
    table_data = table_data.dropna(how='all', axis=1)
    return table_data


pdf_file = extract_gdp_by_country()
table_area = (100, 100, 500, 500)  

# Extract the table from the PDF
table = real_gdp_by_industry(pdf_file, table_area)

# Specify the output CSV file path
output_csv = "data_1-2.csv"

# Save the table data as CSV
table.to_csv(output_csv, index=False)

print(f"Table extracted and saved to {output_csv}")








