import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")


#<span class="titleline"><a href="https://www.apple.com/newsroom/2022/11/emergency-sos-via-satellite-available-today-on-iphone-14-lineup/">Apple: Emergency SOS via satellite available today (US and Canada)</a><span class="sitebit comhead"> (<a href="from?site=apple.com"><span class="sitestr">apple.com</span></a>)</span></span>

myLinks = soup.find_all("span", {"class": "titleline"})


things = ["replit", "python"]

for link in myLinks:
  text = link.text
  textList = text.split()
  containsWord = False
  for word in textList:
    if word.lower() in things:
      containsWord= True
  if containsWord:
    print(link.text)

    myLink = link.find_all("a")
    print(myLink[0]["href"])
