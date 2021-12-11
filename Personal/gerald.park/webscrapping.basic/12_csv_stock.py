from os import write
import requests
import re
import csv
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"}
url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="
for page in range(1, 5):
    res = requests.get(url + str(page),headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <= 1:
        continue
    data =  [columns.get_text().strip() for column in columns]
    print(data)

