import requests
from bs4 import BeautifulSoup


url_stat = 'https://gabestore.ru/game/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
     'Accept-Language': 'ru-RU',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Referer': 'https://google.com/?q=gabestores'
}


while True:
    q = input("enter game \n> ")
    q = q.lower()
    q = q.replace(' ', '-')
    q = q.replace(':', '')
    q = q.replace('™', '')
    q = q.replace('®', '')
    q = q.replace('\'', '')
    url = url_stat + q
    r = requests.get(url, headers=headers)
    print(url + '\n')
    if str(r) == '<Response [404]>':
        r = requests.get(url+'steam', headers=headers)
        if str(r) == '<Response [404]>':
            r = requests.get(url+'origin', headers=headers)
            if str(r) == '<Response [404]>':
                r = requests.get(url+'uplay', headers=headers)
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
    div = soup_main.findAll("div", class_="b-card__table b-card__table--sys")
    soup_sys = BeautifulSoup(str(div), 'html.parser')
    sys = soup_sys.get_text()
    print(sys)
    #------------------



