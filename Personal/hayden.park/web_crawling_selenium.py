import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


URL = 'https://www.kfcc.co.kr/map/view.do?gmgoCd=3808&name=%ED%8F%89%EB%8F%99&gmgoNm=%ED%8F%89%EB%8F%99&divCd=004&divNm=%EA%B3%A0%EC%83%89%EB%8F%99&gmgoType=%EC%A7%80%EC%97%AD&telephone=031-294-4116&fax=031-297-7444&addr=%EA%B2%BD%EA%B8%B0+%EC%88%98%EC%9B%90%EC%8B%9C+%EA%B6%8C%EC%84%A0%EA%B5%AC+%EB%A7%A4%EC%86%A1%EA%B3%A0%EC%83%89%EB%A1%9C+740&r1=%EA%B2%BD%EA%B8%B0&r2=%EC%88%98%EC%9B%90%EC%8B%9C&code1=3808&code2=004&sel=&key=&tab=sub_tab_rate'

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

search = driver.find_elements_by_xpath('//td')
print(search)