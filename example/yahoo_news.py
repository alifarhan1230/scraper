import csv
import requests
from bs4 import BeautifulSoup

# Define the URL of the Yahoo Finance News website
url = "https://finance.yahoo.com/news/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

main_titles = []
titiles = []
content =[]

# Find all market update titles
li_elements = soup.find_all("li", class_="js-stream-content Pos(r)")

with open("yahoo_finance_news.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Content"])

    # Iterate over each <li> element and extract the <h3> and <p> elements
    for li in li_elements:
        # Find the <h3> element within the <li>
        h3_element = li.find("h3")
        # Find the <p> element within the <li>
        p_element = li.find("p")

        # Get the text content of the elements or an empty string if they don't exist
        title = h3_element.text.strip() if h3_element else ""
        content = p_element.text.strip() if p_element else ""

        # Write the data to the CSV
        writer.writerow([title, content])


