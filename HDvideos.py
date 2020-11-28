import requests
from bs4 import BeautifulSoup

headers =  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

url = 'https://hdvideo9.com'
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

for x in soup.find_all('div', class_="upadte"):
    print(x.text, url+
    x.a['href'])
#for link in soup.find_all('a', href=True):
 #   print(link['href'])  
#a = soup.find_all('div', class_="upadte")
#for link in a('a', href=True):
 #   print(link['href'])
