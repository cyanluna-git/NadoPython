import requests
import re
from bs4 import BeautifulSoup

for i in range(1,6):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"}
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)
    res = requests.get(url,headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div",attrs={"class":"name"}).get_text())

    for item in items:

        #광고 제품 제외
        ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("     <광고상품제외>")
            continue

        #리뷰 100개 이상 평점 4.5이상 

        name = items[0].find("div",attrs={"class":"name"}).get_text()
        price = items[0].find("strong",attrs={"class":"price-value"}).get_text()
        rate = items[0].find("em",attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            # print("   <평점없는 상품 제외>")
            continue

        rating_count = items[0].find("span",attrs={"class":"rating-total-count"})
        if rating_count:
            rating_count = rating_count.get_text()[1:-1]
        else:
            # print("   <평점수 없는 상품 제외>")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) > 4.0 and int(rating_count) > 100:
            print(name,price,rate,rating_count)
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rate}점 ({rating_count}개")
            print("바로가기: {}".format("https://www.coupang.com"+link))
            print("-"*100)
