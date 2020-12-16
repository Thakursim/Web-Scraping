import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
           
new_arrivals_url = 'https://www.beinghumanclothing.com/new-arrivals-being-human&sort=sort_order&order=desc&page={}&is_ajax=1'   
for x in range(1, 8):
    scrape_url = new_arrivals_url.format(x)
    result = requests.get(scrape_url, headers=headers)
    json_text = result.json()
    product = json_text[0]
    Bsoup = bs4.BeautifulSoup(product, "html")
    product_name = Bsoup.find_all('h4', class_="product-name")
    for y in product_name:
        New_arrivals = "New-Arrivals", "->", y.text.strip()
        f = open("Being--Human.txt", "a+")
        n_str = " ".join(New_arrivals)
        if len(New_arrivals) > 0:
            f.write("\n")
        f.write(n_str)
        f.close()
men_url = "https://www.beinghumanclothing.com/being-human-men&sort=sort_order&order=desc&page={}&is_ajax=1"
for n in range(1, 26):
    base_url = men_url.format(n)
    res = requests.get(base_url, headers=headers)
    men_text = res.json()
    men_product = men_text[0]
    BSoup = bs4.BeautifulSoup(men_product, 'html')
    product_name_men = BSoup.find_all('h4', class_="product-name")
    for m in product_name_men:
        Men = "Men", "->", m.text.strip()
        f = open("Being--Human.txt", "a+")
        m_str = " ".join(Men)
        if len(Men) > 0:
            f.write("\n")
        f.write(m_str)
        f.close()
mask_url = "https://www.beinghumanclothing.com/being-human-face-masks?plist=4"
Result = requests.get(mask_url, headers=headers)
soup = bs4.BeautifulSoup(Result.text, "html")
mask_product_name = soup.find_all('h4', class_="product-name")
for a in mask_product_name:
    Mask = "Mask", "->", a.text.strip()
    f = open("Being--Human.txt", "a+")
    mask_str = " ".join(Mask)
    if len(Mask) > 0:
        f.write("\n")
    f.write(mask_str)
    f.close()
            