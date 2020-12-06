#------------
# Pekaby 
# https://github.com/pekaby
#-----------
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from fuzzywuzzy import fuzz
import time
import os
import glob


url_stat = 'https://gabestore.ru/game/'
steam_search_url = 'https://store.steampowered.com/search/?term='

get_ru_lang = '?l=russian'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
     'Accept-Language': 'ru-RU',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Referer': 'https://google.com/?q=gabestores'
}

path_to_img = 'images/'

y = "https://static.gabestore.ru/screen_product/"
yt = "https://youtube.com"
def download(link, name):
    global path_to_img
    urlretrieve(link, path_to_img+name+'.png')

def get_link_for_steam(game):
    pass

def search_steam(name):
    global steam_search_url
    global headers
    name = name.replace(' ', '+')
    r = requests.get(steam_search_url + str(name), headers=headers)
    q = BeautifulSoup(str(r.text), 'html.parser')
    print(q.prettify())

print("Written by Pekaby. | https://github.com/Pekaby")
while True:
    i = 0
    q = input("enter game \n> ")
    orig = q

    q = q.lower()
    q = q.replace(' ', '-')
    q = q.replace(':', '')
    q = q.replace('™', '')
    q = q.replace('®', '')
    q = q.replace('\'', '')
    q = q.replace('---', '-')
    q = q.replace('-–-', '-')
    q = q.replace('.', '')
    # search_steam(q)





    url = url_stat + q
    print("LOADING... \n \n")
    r = requests.get(url, headers=headers)
    print(url + '\n')
    if str(r) == '<Response [404]>':
        r = requests.get(url+'-steam', headers=headers)
        if str(r) == '<Response [404]>':
            r = requests.get(url+'-origin', headers=headers)
            if str(r) == '<Response [404]>':
                r = requests.get(url+'-uplay', headers=headers)
                if str(r) == '<Response [404]>':
                    print('404 ' + q)
    soup_main = BeautifulSoup(str(r.text), 'html.parser')

    div = soup_main.findAll("div", class_= "b-card__tabdescription")

    #Description----------
    soup_d = BeautifulSoup(str(div), 'html.parser')
    Description = soup_d.get_text()
    print(Description)
    input()
    #----------------------

    #System-requirements
    # div = soup_main.findAll("div", class_="b-card__table b-card__table--sys")
    # soup_sys = BeautifulSoup(str(div), 'html.parser')
    # sys = soup_sys.get_text()
    # print(sys)
    #------------------
    #additinal information
    div = soup_main.findAll("div", class_="b-card__table")
    desc = BeautifulSoup(str(div), 'html.parser')
    echo = desc.get_text()
    print(echo)
    card_multy = soup_main.findAll("div", class_="b-card__extendinfo")
    card_multy1 = BeautifulSoup(str(card_multy), 'html.parser')
    for b in card_multy1.findAll("div", attrs={'data-title' : True}):
        print(b['data-title'], '\n')
    #-----------
    input()

    #Get YouTube trailer.. or not-------
    get_dive = soup_main.findAll("div", class_="b-card__slider-image--videopreview")
    soup_link = BeautifulSoup(str(get_dive), 'html.parser')
    for a in soup_link.find_all('a', href=True):
        print(a['href'].strip())
    #-------
    input()
    #Get images-------------
    dv = soup_main.findAll("div", class_="b-card__slider-image")
    a1 = BeautifulSoup(str(dv), 'html.parser')
    a = a1.findAll("a", class_="js-fb")
    mainimg = soup_main.findAll("div", class_="b-card__img")
    m = BeautifulSoup(str(mainimg), 'html.parser')
    qqqq = m.findAll("img", class_="js-img-bgcolro")
    for test in qqqq:
        download(str(test['src']), 'main')
    
    for link in a:
        uri = link.get('href')
        if int(fuzz.partial_ratio(str(link.get('href')), y) ) == 100:
            download(uri, str(i))
            print(uri)
            i = i+1
            print('Downloaded. \n')
            # time.sleep(3)
    input("Enter to Delete all images")
    img_files_folder = glob.glob(path_to_img+'*')
    for f in img_files_folder:
        os.remove(f)
