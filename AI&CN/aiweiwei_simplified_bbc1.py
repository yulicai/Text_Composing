import bs4
import requests
import urllib

url = "http://www.bbc.com/news/world-35299069"

html = requests.get(url).text

#it creates a BeautifulSoup object that parsing the html
soup = bs4.BeautifulSoup(html,'html.parser')
#the css select that we inspected before
contents = soup.select(".story-body__inner")


for content in contents:
    stories = content.select('p')
    for story in stories:
        print story.text.encode('ascii').strip()
        # print story.text.encode('utf-8').strip()
