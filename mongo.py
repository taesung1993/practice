import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

client = MongoClient('localhost', 27017)
db = client.dbsparta

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('.list-wrap > tbody > tr.list > td.info')
rank = 0;
for music in musics:
    title = music.select('a.title')[0].text.strip()
    singer = music.select('a.artist')[0].text
    rank += 1
    print(title, singer)
    db.musics.insert_one({
        'rank': rank,
        'title': title,
        'singer': singer
    })



