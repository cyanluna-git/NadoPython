from os import write
import requests
import re
from bs4 import BeautifulSoup




for year in range(2015,2020):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"}
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url,headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("img",attrs={"class":"thumb_img"})
    for idx, image in enumerate(images):
        print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1),"bw") as f:
            f.write(image_res.content)

        if idx >= 4:
            break