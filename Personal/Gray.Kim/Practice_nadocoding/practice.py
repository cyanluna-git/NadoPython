# 5/29

# print(5)
# print(-10)
# print(3.15)
# print(10102030211301203120)
# print(3-2)
# print(3*4)

# print('풍선')
# print("풍선")
# print("가"*9)

# print(5>10)
# print(False)
# print(not True)

# ------------------------------------------------
    # 애완 동물을 소개해 주세요
# dogname = "연탄"
# age = 4
# is_adult = True

    # + or , 로 대체 가능함 뛰어쓰기 한칸 포함
# print("우리집 강아지는" + dogname + "이고" + str(age) + "살 이에요.") 
# print("우리집 강아지는", dogname, "이고", age, "살 이에요.")

    # 연산자 사용
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)  #2.0

# print(2**3) #2^3
# print(5%3) #나머지 2 
# print(5//3) #몫 1 
# print(3==3) #true
# print(3!=3) #false
# print(not(1==3)) #not 사용

# print((3>0) and (3<5)) #둘다 true
# print((3>0) & (3<5)) #둘다 true

# print((3>0) or (3<5)) #둘다 true
# print((3>0) | (3<5)) #둘다 true

# print(5>4>3) #true

# number = 2 +3 * 4
# print(number)
# number = number +3
# # number += 2  위 동등 표현
# # number *= 2 number /= 2 number -= 2
# print(number)

# print(abs(-5)) #절대값 반환
# print(pow(4,2))  #4^2 = 4*4 = 16
# print(max(5,12))
# print(min(5,12))
# print(round(3.14))
# print(round(4.99))

# from math import *

# print(floor(4.99)) # 4 내림 처리
# print(ceil(3.14)) # 4 올림
# print(sqrt(16)) # 4 제곱근 Sqrt


#-----------------------------------------------------------
#from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성

# print(int(random()*10)) # 1 ~ 10 미만의 임의의 값 생성 / 정수 값 출력
# print(int(random()*10)) # 1 ~ 10 미만의 임의의 값 생성 / 정수 값 출력

# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성 / 정수 값 출력
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성 / 정수 값 출력
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성 / 정수 값 출력

# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성 / 정수 값 출력

# print(randrange(1,46)) # 1~ 46 미만의 임의의 정수 값 생성
# print(randint(1,45))    # 1~ 45 이하의 임의의 값 출력


# Quiz----------------------------
# from random import *
# studyday = randint(4,28)
# print('오프라인 스터디 모임 날짜는 매월', studyday, '일로 선정되었습니다.')


# ----------문자
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# # 뭐이런게 된다냐
# Sentence3 = """
# 나는 소년이고, 
# 파이썬이 쉬워요
# """
# print(Sentence3)


# -------slicing (필요 정보 출력)
# jumin = "990914-1234567"
#
# print("성별 : " + jumin[7])  # string [num] 으로 불러올수 있음
# print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 값을 가져올 수 있음
# print("월 : " + jumin[2:4])
#
# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])

# **************문자열 처리함수 55:21
# Python = "Python is Amazing"
# print(Python.lower())
# # .lower() 소문자 변환
# print(Python.upper())
# print(Python[0].isupper())
# print(len(Python))
# print(Python.replace("Python" ,"Java"))
#
# index = Python.index("n")
# print(index)
# index = Python.index("n",index+1)
# print(index)
#
# print(Python.find("n"))
# print(Python.find("Java"))  # 없을 경우 -1을 반환
# # print(Python.index("Java")) #index에서 없을 경우에는 에러처리
#
# print(Python.count("n"))    # 카운트


# ********************문자열 포맷 1:00:59

# print("a"+"b")  # ab
# print("a","b")  # a b

# 방법 1
# print("나는 %d살입니다." % 20)  # d 는 정수를 입력할 수 있다.
# print("나는 %s을 좋아해요" % "파이썬")    # string -> s
# print("Apple 은 %c로 시작해요." % "A")    # Character -> c

# print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))

# 방법 2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파란","빨간"))
#
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란","빨간"))     # 숫자에 따라서 입력 받은 내용을 넣을 수 있다.


# https://youtu.be/kWiCuklohdY?t=3995

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))

# 방법 4 python 3.6이상부터 가능
#
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# **************** 탈출 문자
# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# \" \' 문장 내에서 따옴표를 사용가능함
# 저는 "나도코딩"입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서는 하나의 \ 경로 출력시
# \r 커서를 맨 앞으로 이동
# print("Red Apple\rPine")    # PineApple
# \b : 백스페이스 한글자 삭제
# print("Redd\bApple")

# \t : 탭

# 퀴즈 3


# ***리스트***
# 리스트 []

# subway = [10,20,30]
# print(subway)

# subway = ["유재석","조세호","박명수"]
# print(subway)
#
# print(subway.index("유재석"))      # index 위치 찾기
# subway.append("하하")     # 리스트의 경우 append 마지막에 추가
# print(subway)

# subway.insert(1,"정형돈")
# print(subway)
#
# print(subway.pop())     # 마지막 번째 내용 찾아서 출력하기
# print(subway)

# subway.append("유재석")
# print(subway.count("유재석"))


# 리스트 정렬도 가능함
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# 순서 뒤집기도 가능함
# num_list.reverse()
# print(num_list)

# 리스트 초기화
# num_list.clear()
# print(num_list)


# 리스트는 한가지 자료형을 지정하는 것이 아니라 같이 사용가능
# mix_list = ["조세호",20,True]
# num_list = [5,2,4,3,1]
# print(mix_list)
# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)


# ***Dictionary***
# Key Value // Key 중복을 허용하지 않음

# cabinet = {"3":"유재석","100":"김태호"}
# print(cabinet["3"])

# print(cabinet[43])  # 키가 없는 경우에는 에러를 발생 멈춤

# print(cabinet.get(3))
# print(cabinet.get(53))  # none 출력
# print(cabinet.get(53, "사용가능"))  # 에러 처리 없는 경우 사용가능으로 출력됨

# print(3 in cabinet)     # True
# print(5 in cabinet)     # False

# new key in
# cabinet["5"] = "김종국"    # 신규 키인
# print(cabinet)
# cabinet["3"]= "유dn재석"       # 기존 내용있을시 덮어쓰기
# print(cabinet)

# del cabinet["5"]
# print(cabinet)

# Key 들만 출격
# print(cabinet.keys())
# Value 들만 출력
# print(cabinet.values())
# 쌍으로 출력
# print(cabinet.items())

# 목욕탕 폐점
# cabinet.clear()     # 리스트 전체 초기화

# ***튜플*** 리스트와 다르게 추가, 변경을 할 수 는 없음 속도는 리스트 보다 빠름

# menu = ("돈까스","치즈까스")
# print(menu[0])

# name = "김종국"
# age = 20
# hobby = "코딩"

# (name, age, hobby) = ("김종국",20,"코딩")
# print(name, age, hobby)

# 집합 (Set)
# 중복안됨, 순서 없음
# my_set = {1,2,3,3,3,}
# print(my_set)       # 중복값에 대해서는 출력 없음 {1,2,3}
#
# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박면수"])

# print(java & python)        # 교집합
# print(java.intersection(python))    # 교집합 '유재석'

# 합집합 java or Python
# print(java | python)
# print(java.union(python))

# 차집합 java 할 수 있지만 Python 은 못하는 개발자
# print(java - python)
# print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남        추가 및 삭제가 가능함
# python.add("김태호")
# print(python)


# ***자료 구조의 변경***   형 변환
# 커피숍
# menu = {"커피","우유","주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu,type(menu))

# menu = set(menu)
# print(menu, type(menu))

# 퀴즈 4

# ****IF***

weather = "비"

# if 조건:
#     실행 명령문


# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 없어요")


# temp = int(input("기온은 어떄요?"))     # int로 형 변환해서 입력함
# if 30 <= temp:
#     print("Hot..")
# elif 10 <= temp and temp <30:
#     print("괜찮으 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")


# ***for***
# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))


# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨","토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# While
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer,index))
#     index-=1
#     if index == 0:
#         print("커피가 폐기")

# while True:



# while person != customer :   # 동일 조건까지 반복함

# absent = [2,5]
# nobook = [7]
# for student in range(1,11):                # absent일 경우에 continue 출력
#     if student in absent:
#         continue
#     elif student in nobook:                 # nobook일 경우 break 반복 문이 있어도 종료
#         print("오늘 수업끝")
#         break
#     print(student)

# **********************for 문 활용
# 출석 번호가 1234, 앞에 100을 붙이기로
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]    # students 값에 i 에 100을 더함
# print(students)

# 학생 이름을 길이로 변환
# students=["Iron man ","thor","i am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생이름을 대문자로 변환
# students=["Iron man ","thor","i am groot"]
# students = [i.upper() for i in students]
# print(students)

# Quiz 5

# *****함수****
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()

# 전달값과 반환값
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance > money:
#         print("출금이 완료되었습니다.".format(balance- money))
#     else:
#         print("출금이 완료되지 않았습니다.")

# def withdraw_night(balance, money):     #밤 출금
#     commision = 100 # 수수료 100원
#     return commision, balance - money - commision   # 튜플 형식으로 반환함

# balance = 0
# balance = deposit(balance,1000)
# print(balance)   # 반환형 지정은 없는듯?

# balance = withdraw(balance,20)
# commission, balance = withdraw_night(balance,500)

# 함수 기본값 설정
# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t주 사용언어: {2}" \
#           .format(name, age, main_lang))

# profile("유재석",20, "파이썬")

# def profiles(name, age=17, main_lang="파이썬"):        #기본값 선 입력해서 사용하기
#     print("이름 : {0}\t 나이 : {1}\t주 사용언어: {2}" \
#           .format(name, age, main_lang))

# profiles("유재석")
# profiles("유재",20)

# 키워드 값 사용하기
# def profile(name, age, main_lang):
#     print(name,age,main_lang)

# profile(main_lang="python", ---)   # 키워드로 전달을 할 수도 있음

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")     #end=" " 해당 문장이 완료된 후 다음에 줄 바꿈하지 않므


# 가변 인자 *language
# def profile(name, age, *language):      # 위 처럼  lang1,2에 대해서 추가하지 않아도됨
#     print("")


# ****지역변수 전역변수****
# gun = 10
# def checkpoint(soilders): # 경계근무
#     global gun      # checkpoint 안에서 이미 선언된 전역변수를 사용하겠다.
#     gun = gun - soilders
#     print(gun)
#
# checkpoint(2)       #error 지역변수 함수 내 변수가 초기화 되지 않음

  # Quiz 6

# ****표준 입출력

# print("Python","Java")
# print("Python","Java", "Javascript", sep=" vs ")      # 사이 반복되는 중복값에 대해서 sep에서 내용 정의 가능함

# print("Python", "java", sep=",",end="?")        # 2개의 print를 한줄에 출력이 가능함
# print("무엇이 더 재밌을까요?")

# import  sys
# print("Python", "java", file=sys.stdout)
# print("Python", "java", file=sys.stderr)


# scores = {"수학":0, "영어":50, "코딩":100}
# print(scores)
# for subject, score in scores.items():
    # print(subject.ljust(8),str(score).rjust(4), sep=":")     # 정렬을 통해서

# 은행 대기순번표
#001,002, 003
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))        # 공간을 차지하며 3칸을 차지하며 남는 값은 0으로 채울수 있음


# 표준 입력
# answer = input("아무 값이나 입려갛세요 : ")         # answer에 입력되는 타입은 str 사용자 입력을 통해서 받게 된 값은 자동으로 STR이다
# print("입력하신 값은"+ answer + "입니다.")

# ***다양한 출력 포맷

# 빈 자리느 ㄴ빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: > 10}".format(500))

# 양수일떄는 +로 표시, 음수 일떈 -로 표시
# print("{0: >+10}".format(500))       # +500
# print("{0: >+10}".format(-500))      # -500

# 왼쪽 정렬하고
# print("{0:_<10}".format(500))       # +500
# 3자리 마다 콤마를 찍기
# print("{0:,}".format(100000000000))
# 3자리 마다 콤마 +- 부호도 붙이기
# print("{0:,}".format(-100000000000))

# 소수점 출력
# print("{0:f}".format(5/3))
# 소수점 특정 자리수까지 출력하기
# print("{0:.2f}".format(5/3))   # 소수점 3째 자리에서 반올림



# *******파일 입출력*******
# score_file = open("score.txt","w",encoding="utf8")       # 쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 10", file=score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8")          #이어쓰기
# score_file.write("과학 : 80")     # Wite에서는 줄바굼이 없음 print에서는 가능
# score_file.write("\n코딩 : 100")
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")                # Read  .read()를 통해서 전체를 읽어 올 수 있음
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")                # Read
# print(score_file.readline())    # 줄 별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# 반복 문 활용 라인 출력하기
# score_file = open("score.txt", "r", encoding="utf8")                # Read
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# list 형태로 출력하기  한줄 씩 불러와서 출력
# score_file = open("score.txt", "r", encoding="utf8")                # Read
# lines = score_file.readlines()      # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


# ***피클*** 사용하고 있는 데이터를 파일로 저장?  // 유용한 라이브러리임

# import pickle

# pickle 형식으로 쓰기
# profile_file = open("profile.pickle", "wb")             # pickle을 쓰기 위해서는 binary type으로 w write
# profile = {"이름": "박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
#
# pickle.dump(profile,profile_file)   # profile에 있는 정보를 file에 저장함
# profile_file.close()

# pickle 형식을 읽어오기
# profile_file = open("profile.pickle", "rb")             # pickle을 쓰기 위해서는 binary type으로
# profile = pickle.load(profile_file)                  # file에 있는 정보를 불러오기
# print(profile)
# profile_file.close()


# ******WITH******* 파일을 열고 처리를 하고 닫는 작업을 했음
# import pickle

# with open("profile.pickle", "rb") as profile_file:      # 파일 내용을 file에 입력하고, with 문을 나오면서 close까지 진행함
#     print(pickle.load(profile_file))


# 읽고 쓰고를 간단히 할수 있으며 열고 닫기 코드가 필요없음
# with open("study.txt", "w", encoding="utf8")  as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())

# Quiz 7


# 9.1 Class $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 마린
# name = "마린"
# hp = 40
# damage = 5  # 유닛의 공격력
# print(name,hp,damage)
#
# # 탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damaga = 35
#
# def attack(name, location, damage):
#     print("{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format( \
#         name, location, damage))
#
# attack(name, "1시" ,damage)


# class 예시 시작
class Unit:
    def __init__(self,name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        # self.damage = damage
        # print("{0} 유닛이 생성 되었습니다.".format(self.name) )
        # print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
              .format(self.name, location, self.speed ))

    def damaged(self,damage):
            print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
            self.hp -= damage
            if self.hp <=0:
                print("{0} : 파괴되었습니다.".format(self.name))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크", 150, 35)


# __init__ 생성자 클래스 객체 동일한 변수를 입력해야됨

# 멤버 변수

#레이스
# wraith1 = Unit("레이스",80,5)
# print(wraith1.hp, wraith1.name)             # 멤버 변수를 외부에서도 사용가능하다]

# wraith2 = Unit("빼앗은 유닛",80,5)
# wraith2.clocking = True    # *******외부에서 객체의 멤버 변수를 확장할 수 있음 기존 객체에는 해당 내용 반영 없음

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 공격 유닛
class AttackUnit(Unit):         # 공격 유닛은 유닛을 상속받아서 사용됨
    def __init__(self,name, hp, speed, damage):
        # self.name = name
        # self.hp = hp
        # 유닛 상속
        Unit.__init__(self,name,hp, speed)
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name) )
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}" \
              .format(self.name, location, self.damage))


# 파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중 상속
# 부모 클래스를 2개 이상 상속 받는 경우에?

# 드랍쉽 공격은 불가함
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
              .format(name, location, self.flying_speed))
# 다중상속됨
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self,name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name,hp, 0, damage)          # 지상 스피드느 0으로 출력
        Flyable.__init__(self,flying_speed)

    def move(self, location):           #연산자 오버로딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
# valkyrie = FlyableAttackUnit("발키리", 200, 6,5)
# valkyrie.fly(valkyrie.name,"3시")

# 연산자 오버로딩 // 부모클래스에서 선언된 내용을 자식 클래스에서 변경하여 사용 오버로딩'

#
# #벌쳐
# Vulture = AttackUnit("벌쳐",80,10, 20)
# #배틀크루저
# battlecruiser = FlyableAttackUnit("배틀크루저",500, 25, 3)
#
# Vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")             # 지상, 공중 유닛을 구분하여서 move fly를 사용해야됨
#
# # 연산자 오버로딩//fly --> move
# battlecruiser.move("11시")



# ****Pass****

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self,name,hp,0)
#         super().__init__(name, hp,0)    # self를 입력하지 않아도됨, 다중 상속시에는 문제가 됨 / 최우선 상속 클래스만 지칭 가능함 / 모든 부모 클래스에 대한 초기화가 필요할 경우 명시적으로 표기해줘야됨
#         # pass            # 정의된 내용을 완성하지 않고 미리 작업을 추가함?

# # 서플라이 디폿
# supply_depot = BuildingUnit("서플라이",500, "7시")
    
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    #스팀팩
    def stimpack(self):
        if self.hp  > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
# 탱크
class Tank(AttackUnit):
    #시즈모드
    seize_developed = False #개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150,1,35)
        self.seize_mode = False 

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 시즈모드 X
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 시즈모드 O -> 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__("레이스",80,20,5)
        self.clocked = False    # 해제 상태
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다." .format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = True