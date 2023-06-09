import csv
import requests
from bs4 import BeautifulSoup


def spglobal_research_insights_economic_data():

    base_url = 'https://www.spglobal.com/marketintelligence/en/mi/research-analysis/economics-country-risk.html'
    req = requests.get(base_url)
    # for page in range(1, 8):
        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main_element = soup.find('ol', 'search-results')
    items = main_element.find_all('li')
        
    datas = []
    for item in items:
        try: title = ''.join(item.find('div', class_='searchresultTilte').text.strip().split('\n'))
        except:title = ''
        
        try: content = ''.join(item.find('p', class_='content-display').text.strip().split('\n'))
        except:content = ''
        datas.append([title, content])
       
        
    header_csv = ['Title', 'Content']
    writer = csv.writer(open('csv/spGlobal-economic-research.csv', 'w', newline=''))
    writer.writerow(header_csv)
    for data in datas: writer.writerow(data)
    
    print("CSV file has been created successfully.")
          
          
def spglobal_research_insights_emerging_markets():
    base_url = 'https://www.spglobal.com/en/research-insights/topics/emerging-markets';
    req = requests.get(base_url)
        
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    card_content_elements = soup.find_all('div', class_='card__content')

    # Extract the text from each <div class="card__content"> element
    titles = [element.get_text(strip=True) for element in card_content_elements]

    header = ['content']

    with open('csv/spGlobal-economic-emerging-market.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(zip(titles))

    print("CSV file has been created successfully.")
        
    
    
spglobal_research_insights_economic_data()
spglobal_research_insights_emerging_markets()
