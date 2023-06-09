import requests
from bs4 import BeautifulSoup
import pandas as pd

def economist():
    params = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'P', 'W', 'X', 'Y', 'Z']
    
    for param in params:  
        print(f"append data page: {param}")
        base_url = f'https://www.economist.com/economics-a-to-z#{param}'
        req = requests.get(base_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
        main_element = soup.find('dl')
        dt_elements = main_element.find_all('dt')
        dd_elements = main_element.find_all('dd')
        
        data = []
        
        for dt, dd in zip(dt_elements, dd_elements):
            dt_text = dt.get_text().replace('\n', ' ')
            dd_text = dd.get_text().replace('\n', ' ')
            data.append([dt_text, dd_text])
        
        header_csv = ['Title', 'Content']
        df = pd.DataFrame(data, columns=header_csv)
        df.to_csv('csv/economist.csv', mode='a', header=False, index=False)
        
    print("Data appended to CSV file successfully..")


economist()