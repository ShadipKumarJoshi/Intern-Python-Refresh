# Write a program that installs and uses an external package like requests (bonus: fetch a webpage title).

#  pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

#  IMDb URL
url ='https://www.example.com'

# Send request to the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

#  Extract the title of the tag content
title = soup.title.string if soup.title else "NO title found"

print("Webpage Title:", title)
