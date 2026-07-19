# &&&&&&&&&&&&모듈******************* 유지보수 및 코드의 재 사용성을 위해서 중요

# https://youtu.be/kWiCuklohdY?t=19011
# 11.1 모듈

# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people,people * 4000))

