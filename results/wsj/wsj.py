from requests_html import HTMLSession
import requests
import json

session = HTMLSession()

url = 'https://www.wsj.com/pro/venture-capital/industry-news'

request = session.get(url)
print('Waiting for scraping WSJ...')

request.html.render(sleep=1, scrolldown=20)

articles = request.html.find('article')

# Make URLs
def get_link_news():
    links = []
    for item in articles:
        id_news = item.attrs['data-id']
        link = f"https://www.wsj.com/pro/venture-capital/industry-news?id={id_news}&type=article%7Ccapi"
        links.append(link)

    try:
        print("Fetching news...")
        for url in links:
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if 'headline' in data and 'summary' in data:
                        headline = data['headline']
                        summary = data['summary']
                        print(f"Headline: {headline}")
                        print(f"Summary: {summary}")
                    else:
                        print("Headline or summary not found in the response")
                except json.JSONDecodeError:
                    print("Invalid JSON in the response")
            else:
                print(f"Failed to fetch data for URL: {url}")
                
            print("Response text::", response.text)

    except Exception as e:
        print(f'Error: {e}')


get_link_news()
