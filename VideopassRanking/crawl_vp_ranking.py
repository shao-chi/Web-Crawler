import requests
from bs4 import BeautifulSoup
from datetime import datetime
# import os
import json

date = datetime.strftime(datetime.today(), '%Y%m%d')
# os.mkdir('./{}'.format(date))
f = open('./{}.txt'.format(date), 'w')

drama_rank = []
rank = 0
for i in range(1, 15):
    url = "https://www.videopass.jp/genres/21?license=unlimited&page={}".format(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")
    name = soup.select("div.vdcard__name")

    for j in range(len(name)):
        drama_ranking = {}
        rank += 1
        drama_ranking['rank'] = rank
        drama_ranking['name'] = name[j].text
        drama_rank.append(drama_ranking)

jp_rank = []
rank = 0
for i in range(1, 7):
    url = "https://www.videopass.jp/genres/21/23?license=unlimited&sort=popular&hd=0&page={}".format(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")
    name = soup.select("div.vdcard__name")

    for j in range(len(name)):
        jp_ranking = {}
        rank += 1
        jp_ranking['rank'] = rank
        jp_ranking['name'] = name[j].text
        jp_rank.append(jp_ranking)

ko_rank = []
rank = 0
for i in range(1, 4):
    url = "https://www.videopass.jp/genres/21/25?license=unlimited&sort=popular&hd=0&page={}".format(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")
    name = soup.select("div.vdcard__name")

    for j in range(len(name)):
        ko_ranking = {}
        rank += 1
        ko_ranking['rank'] = rank
        ko_ranking['name'] = name[j].text
        ko_rank.append(ko_ranking)

am_rank = []
rank = 0
for i in range(1, 16):
    url = "https://www.videopass.jp/genres/26/26?license=unlimited&sort=popular&hd=0&page={}".format(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")
    name = soup.select("div.vdcard__name")

    for j in range(len(name)):
        am_ranking = {}
        rank += 1
        am_ranking['rank'] = rank
        am_ranking['name'] = name[j].text
        am_rank.append(am_ranking)

ranking = {'drama_ranking': drama_rank,'jp_ranking': jp_rank, 'ko_ranking': ko_rank, 'am_ranking': am_rank}
f.write(json.dumps(ranking, ensure_ascii=False))
# f.write(str(ranking))
f.close()