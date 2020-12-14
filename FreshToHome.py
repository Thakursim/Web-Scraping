import requests
import bs4
import math

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
cat_no = [18, 19, 20, 25, 26, 28, 29, 31, 32, 34, 40, 42, 53, 58, 59, 60, 63, 65, 72, 74, 75, 76, 77, 78, 79, 82, 84, 86, 87, 88, 92, 94]
           
for x in cat_no:
    url = 'https://www.freshtohome.com/all-products?cat={}'
    scrape_url = url.format(x)
    new_url = scrape_url + '&p=1'
    new_res = requests.get(new_url, headers=headers)
    new_soup = bs4.BeautifulSoup(new_res.text, 'html')
    page_no = new_soup.find('p', class_='amount')
    #print(page_no.text)
    #print(page_no.text.strip().split(" "))
    text = page_no.text.strip().split(" ")[-2]
    a = (int(text))
    num = math.ceil(a/60)
    print(num)
    for z in range(1, num+1):
        actual_url = scrape_url + '&p={}'
        base_url = actual_url.format(z)
        print(base_url)
        result = requests.get(base_url, headers=headers)
        Bsoup = bs4.BeautifulSoup(result.text, 'html')
        cat_name = Bsoup.find_all('span', class_="value")        
        for n in cat_name:        
            category = n.text
            pages = Bsoup.find_all('h3', itemprop="name")
            for y in pages:
                text = category ,'->', y.text 
                text_str = "".join(text)
                f = open('FreshToHome.txt', 'a+', encoding="utf-8")
                if len(text) > 0:
                    f.write("\n")
                f.write(text_str)
                f.close()