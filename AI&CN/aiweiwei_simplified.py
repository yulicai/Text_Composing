import bs4
import requests
import urllib

url = "https://www.nytimes.com/2014/09/21/arts/design/ai-weiwei-takes-his-work-to-a-prison.html"

html = requests.get(url).text

#it creates a BeautifulSoup object that parsing the html
soup = bs4.BeautifulSoup(html,'html.parser')
#the css select that we inspected before
contents = soup.find_all("p",class_= "story-body-text story-content")


for content in contents:
    #ascii for text blob to analyze, it cant handle utf-8
    print content.text.encode("ascii","ignore").strip()
    # print content.text
