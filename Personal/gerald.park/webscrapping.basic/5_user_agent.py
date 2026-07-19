import requests 
url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"}
res=requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html","w", encoding="utf8") as f:
    f.write(res.text)