import csv
import requests
from bs4 import BeautifulSoup

# Define the URL of the Yahoo Finance News website
url = "https://finance.yahoo.com/topic/stock-market-news/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")


# Find all market update titles
li_elements = soup.find_all("li", class_="js-stream-content Pos(r)")



with open("market.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title",  "Content"])

    # Iterate over each <li> element and extract the <h3>, <a>, and <p> elements
    for li in li_elements:
        # Find the <h3> element within the <li>
        h3_element = li.find("h3")
        title = h3_element.text.strip() if h3_element else ""

        # Find the <p> element within the <li>
        p_element = li.find("p")
        content = p_element.text.strip() if p_element else ""

        # Write the data to the CSV
        writer.writerow([title, content])
