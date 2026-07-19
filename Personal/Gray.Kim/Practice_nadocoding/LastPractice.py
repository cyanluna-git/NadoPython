# *********** 10-1 예외 처리 ***************** 에러 발생시
# 계산기

# try:                # Try Catch
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     # num1 = int(input("첫번쨰 숫자를 입력하세요 : "))
#     # num2 = int(input("두번쨰 숫자를 입력하세요 : "))
#     nums.append(int(input("첫번쨰 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번쨰 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생했습니다.")
#     print(err)



# *******10-2,3,4 에러 발생시키기*********

# &&&&&&&&&&&&&에러코드 제작하기&&&&&&&&&&&&
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return  self.msg
#
# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번쨰 숫자를 입력하세요 : "))
#     num2 = int(input("두번쨰 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise  BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요")
#     print(err)          # 문제가 발생시 위에서 입력한 내용을 받아와서 출력을 하게됨
#
# # finally 예외처리에 상관없이 항상 마지막에 동작할 수 있도록 하는 것
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")


# 예외처리를 통해서 없는 파일에 접근, 리스트 내 없는 인덱스 등 처리 / 완성도를 높임



# Quiz 9 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# 치킨집, 대기 손님, 자동 주문 시스템, 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
# 출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
# 치킨 소진 시 사용자 정의 에러 SoldOutError를 발생시키고 프로그램 종료
# 출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드] **********************

# class SoldOutError(Exception):
#     pass
#
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석 대기번호 1부터 시작
# while(True):
#     try:
#         print("[남은 치킨 : {0}".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠씁니까?"))     # 문자열 입력시 int로 변환되면서 error 발생 except이동
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                   .format(waiting,order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break


# ********************** 11-1 모듈 사용을 통한 개발 / Theatre_module
# 모듈을 쓰려는 같은 경로에 있거나 Python 라이브러리가 모여있는 같은 경로에 있어야 사용이 가능함
# 예제는 같은 workspace에 있어서 가능함

# import theater_module as tm
# tm.price(3)
# tm.price_morning(4)
# tm.price_soldier(5)
#
# # from import
# from theater_module import *    # module에 있는 전체 내용을 쓰겠다. 위와 동일함
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning         # 필요한 함수에 대해서만 호출해서 사용할 수 있따.
# price(5)
# price_morning(6)
# # price_soldier(7) 호출을 하지 않은 함수는 에러 발생
#
# from theater_module import price_soldier as price       # 선택한 함수를 다른 명칭으로 변경 할 수 도 있다.
# price(5)    # 실제는 price_soldier




# ************* 11-2 패키지***************
# 모듈들을 모아둔 집합 / 하나의 디렉토리에 많은 모듈을 저장해둠

# import travel.thailand      # Travel 패키지 안에 있는 thailand 모듈을 사용 가능함 / 가장 마지막에는 모듈이나 패키지 레벨까지만 가능 / 클래스나 함수는 직접 import 못함
# # import travel.thailand.ThailandPackage        # 다음과 같이 import 시 에러발생함
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# # from 절에서는 클래스 함수까지도 가능함 / 모듈이나 패키지, 클래스 함수까지도 import 가능함 from 절!
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import  vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 11-3 _all- ******************************

# # from random import *  # ramdom 내 모든 내용을 쓰겠다.
# from travel import *        # travel 내 모든 내용을 가져오겠다.. / 개발자가 공개 범위를 지정해줘야됨 __init__에서 / __all__ 로 공개 범위 지정가능
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
#
# trip_to1 = thailand.ThailandPackage()
# trip_to1.detail()


# 11-4 모듈 직접 실행 *********************
# 모듈 제작후 테스트를 위한 경우 직접 실행
# Thailand.py


# # 11.5 패키지, 모듈 위치 찾기 ***********************
# import inspect
# import random
# from travel_test import *   # random.py 경로에 travel_test 생성함
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# 11.6 pip install / 이미 개발된 패키지를 사용하여 생산성을 높임 / 기본 제공 외에
# https://pypi.org/search/

# beautifulsoup
# pip install beautifulsoup4

# 예제 출력
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# pip list / 설치된 pip 확인 가능
# pip show beautifulsoup4  / 상세 정보 출력
# pip install --upgrade beautifulsoup4 / upgrade 시
# pip uninstall beautifulsoup4 / uninstall 시


# 11.7 내장 함수 / 추가 설치 없이 기존 내장되어 있는 함수

# # input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}" , .format(language))

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())

# print(dir())
# import random   # 외장함수
# print(dir())        # import 전과 다르게 random이 추가로 사용가능하도록 생성됨
# import pickle
# print(dir())        # import pickle 추가

# print(dir(random))      # random 내에서 사용가능한 출력 random.

# lst = [1,2,3,]
# print(dir(lst))

# name = "가나다"        # 자료형에 따라 사용가능한 메소드 출력
# print(dir(name))

# list of python builtin  검색을 통해서 추가로 확인 가능 / https://docs.python.org/3/library/functions.html



# 11.8 외장 함수 / 직접 import 해서 사용해야됨
# https://docs.python.org/3/py-modindex.html        / 외장함수 목록 및 예제

# # glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir과 동일)
# import  glob
# print(glob.glob("*.py"))    # 확장자가 py인 모든 파일 조회


# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리
#
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# import  os
# print(os.listdir())     # glob과 동일하게 dir


# # time : 시간 관련 함수를 제공
# import  time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))


# import datetime
# print("오늘 날짜는 ",datetime.date.today())
#
# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()   # 오늘 날자 저장
# td = datetime.timedelta(days=100)   # 100일 저장
#
# print("우리가 만난지 100일", today + td)   # 100일 후


# Quiz 10
# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건: 모듈 파일명은 byme.py로 작성
#
# (모듈사용 예제)
# import byme
# byme.sign()
#
# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어짐
# 유튜브 : --
# 이메일 : --