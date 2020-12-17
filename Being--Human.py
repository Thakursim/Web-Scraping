import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
           
b = [{"url": "https://www.beinghumanclothing.com/new-arrivals-being-human&sort=sort_order&order=desc&page=%s&is_ajax=1", "page_count": 8, "desc": "New-arrivals"}, {"url": "https://www.beinghumanclothing.com/being-human-men&sort=sort_order&order=desc&page=%s&is_ajax=1", "page_count": 26,
"desc": "Men"}, {"url" : "https://www.beinghumanclothing.com/being-human-face-masks&page=%s&is_ajax=1", "page_count": 2, "desc": "Mask"}]	
	
for x in b:
    for no in range(1, x['page_count']):
        base_url = x['url'] % (no)
        res = requests.get(base_url, headers=headers)
        json_text = res.json()
        product = json_text[0]
        soup = bs4.BeautifulSoup(product, 'html')
        product_name = soup.find_all('h4', class_='product-name')
        for n in product_name:
            list_of_products = x['desc'],"->", n.text.strip()
            f = open("Being--Human.txt", "a+")
            str_list = " ".join(list_of_products)
            if len(list_of_products) > 0:
               f.write("\n")
            f.write(str_list)
            f.close()
            