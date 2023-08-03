import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.cyclobold.com/")
soup = BeautifulSoup(r.content, "html.parser")
data = soup.prettify()
headings = soup.find_all("form")
print(headings)

# print(headings.text)
heading = ""
for heading in headings:
    print(heading)