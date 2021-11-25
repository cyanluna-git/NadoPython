import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs) # 속성정보 반환
# print(soup.a["href"]) # href 속성 값 반환 

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank4 = rank3.find_next_sibling("li")
# print(rank4.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="독립일기")
print(webtoon)