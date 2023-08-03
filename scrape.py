import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.netflix.com/ng/")

soup = BeautifulSoup(r.content, 'html.parser')
data = soup.prettify()
images = soup.find_all("p")
# print(images)
for image in images:
    print(image)
