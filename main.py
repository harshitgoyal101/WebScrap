import requests
from bs4 import BeautifulSoup

URL = "https://www.airbnb.co.in/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') 
 
def get_categories():
    categories = []  
    for row in soup.findAll('span', attrs = {'class': "c1ozl2w2 atm_9s_1txwivl atm_ar_1bp4okc atm_h_1h6ojuz atm_jb_1sx8fo5 atm_cx_evh4rp atm_cx_1yuitx__oggzyc dir dir-ltr"}):
        categories.append({
            "label": row.find('span', attrs = {'class': "ti7yjx atm_ve_glywfm atm_vb_glywfm atm_9s_1o8liyq atm_uc_1bfgeka dir dir-ltr"}).text,
            "src":  row.find('img')['src']
        })
    return categories

print(get_categories())