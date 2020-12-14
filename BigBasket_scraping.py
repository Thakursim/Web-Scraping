import requests
import bs4
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
url = 'https://www.bigbasket.com/product/all-categories/'
res = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(res.text, 'html')
drop_down = soup.find_all('div', class_='DropDownColum')
for x in drop_down:
    slug = x.a['href'].split("/")[3]
    parent = x.a['href'].split("/")[2]
    url_new = 'https://www.bigbasket.com/product/get-products/?slug={}&tab_type=[%22all%22]&sorted_on=popularity&listtype=pc'.format(slug)
    base_url = url_new + "&page={}"
    for x in range(0, 1000):
        scrape_url = base_url.format(x)
        res = requests.get(scrape_url)
        json_text = res.json()
        if isinstance(json_text['tab_info'], list):
            condition = json_text['tab_info'][0]['product_info']['products']
            if len(condition) == 0: 
                break
        else:
            condition = json_text['tab_info']['product_map']['all']['prods']
            if len(condition) == 0:
                break
        for y in range(0, len(condition)):
            if isinstance(json_text['tab_info'], list):
                products = parent, '->', slug, '->' ,json_text['tab_info'][0]['product_info']['products'][y]['p_desc']
                #print(products)
            else:
                products = parent, '->', slug, '->' , json_text['tab_info']['product_map']['all']['prods'][y]['p_desc']
                #print(products1)
            f = open('BBscraping.txt', 'a+')
            products_str = " ".join(products)
            print(products_str)
            if len(products) > 0:  
                f.write("\n")
            f.write(products_str)
            f.close()
                # print(products_str)
                # print(products1_str)