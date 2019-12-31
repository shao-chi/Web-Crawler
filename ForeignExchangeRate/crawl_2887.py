import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import pandas as pd

data = []

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
url="http://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
driver.get(url)

select_y = Select(driver.find_element_by_name('yy'))
select_y.select_by_value("2002")
select_m = Select(driver.find_element_by_name('mm'))
select_m.select_by_value("2")
driver.find_element_by_name("stockNo").send_keys("2887")
driver.find_element_by_xpath("//*[@class='button search']").click()

soup = BeautifulSoup(driver.page_source,"html.parser") #將網頁資料以html.parser
date = soup.select("td.dt-head-center") #取HTML標中的 <td class="text-center"></td> 中的<a>標籤存入sel
print(date[0].text)
# for i in range(0,len(sel),2):
#     data.append({'date': sel[i].text, 'buy_in': buy_in[i].text, 'sell_out': buy_in[i+1].text})

# data_df = pd.DataFrame(data)
# data_df.to_csv('2887_20180214'.csv', encoding='utf-8')
# print(data_df)