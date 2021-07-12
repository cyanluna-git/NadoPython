# a = 1
# b = 2
# # if a > b: # 같다
# # if a == b: # 같다
# if a != b: # 다르다 
# # if a >= b: # GT Greater than 
# # if a <= b: # LT Less than 
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
# IF 비교연산자 
# money = 2000
# if money < 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")


# AND OR NOT

# OR
# if False or False:
# if False | False: # 이것도 OR

# AND
# if True and True:
# if True & False: # 이것도 AND 
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# in 들어 있으면 TRUE
# Not in 안들어 있으면 TRUE
# # in, not in 은 따로 기호가 없음 
# if 1 in [1,2,3]:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")


# if 1 in [1,2,3]:
#     print("택시를 타고 가라")
# else:
#     pass # 아무것도 하고 싶지않을때

#  다중 분기 
# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket:
#     print("택시를 타고 가라")
# elif card: 
#     print("택시를 타고 가라")
# else: # 아니면 ~ 앞에조건이 다 False이면 실행하는 제어문 
#     print("걸어가라")

score = 70
if score > 60:
    message = 'success'
else:
    message = 60 

# 위에 5줄을 한줄로 만들기 
message = "success" if score > 60 else "failure" # 조건연산자 한줄에 if문 다쓰기. 

# 반복문 

## 이거 실습한 코드는 Github에 올려주세요 ~ 
## Lisa님 코드 올려주신거 확인했어요 수고하셨습니다~ 

#while 
treeHit = 0 
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

# 디버깅은 예상안했는데 이것까지 알려주네요.ㅎㅎ 
# 종료 2분 전입니다~ 
# 실습해보시고 이해안가는 부분이 있으면 물어봐주세요. 
