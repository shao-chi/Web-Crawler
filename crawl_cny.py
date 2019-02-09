import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for i in range(1,13):
    if i < 10:
        url="https://rate.bot.com.tw/xrt/quote/2018-0{}/CNY".format(i)
    else:
        url="https://rate.bot.com.tw/xrt/quote/2018-{}/CNY".format(i)
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    sel = soup.select("td.text-center") #取HTML標中的 <td class="text-center"></td> 中的<a>標籤存入sel
    buy_in = soup.select("td.rate-content-cash")
    for i in range(0,len(sel),2):
        data.append({'date': sel[i].text, 'buy_in': buy_in[i].text, 'sell_out': buy_in[i+1].text})
        
url="https://rate.bot.com.tw/xrt/quote/2019-01/CNY"
print(url)
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel = soup.select("td.text-center") #取HTML標中的 <td class="text-center"></td> 中的<a>標籤存入sel
buy_in = soup.select("td.rate-content-cash")
for i in range(0,len(sel),2):
    data.append({'date': sel[i].text, 'buy_in':buy_in[i].text, 'sell_out': buy_in[i+1].text})

data_df = pd.DataFrame(data)
data_df.to_csv('cny201801~.csv', encoding='utf-8')
print(data_df)