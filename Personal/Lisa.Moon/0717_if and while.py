#Jo Coding 제어문

# money = True
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# a=1
# b=2
# if a>b:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# *******이거 다시 보기 이해 안감.........******************
# money = 2000
# card=1
# if money >=3000 | card :
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# money = 2000
# card=1
# if 1 in [1,2,3]:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# pocket = ['paper', 'cellphone']
# card=1
# if 'money' in [pocket] :
#     print("택시를 타고 가라")
# #한번 더 조건을 주는것! elif 여러번 반복적으로 사용 가능 (elseif)
# elif card:
#     print("택시를 타고 가랏")
# else:
#     print("걸어가라")


# score = 70
# if score>= 60:
#     message = "success"
# else:
#     message = "fail"
# print(message)

#조건부 표헌식 : 위의 코드를 한줄로 & 조건부표헌식 할때는 else 꼭 써줘야함 아님 error
# score=50
# message = "success" if score >=60 else "fail"
# print(message)

#반복문 (while문)
# treehit = 0
# while treehit < 10:
#     treehit = treehit +1
#     print ("나무를 %d번 찍었습니다." %treehit)
#     if treehit == 10:
#         print("나무 넘어갑니당")

# while and break 
# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다")
#     coffee = coffee -1
#     print("남은 커피는 %d잔 입니다" %coffee)
#     if not coffee:
#         print("커피가 다 떨어졌습니다! 판매 종료합니다")
#         break #break를 써서 while문을 종료시키는것 

#while and continue
a=0
while a<10:
    a = a+1
    if a %2 == 0:
        continue #continue 조건을 만족하면(여기서는 짝수이면~~) 그 밑으로 넘어가지 않고 while 문의 처음오로 가서 다시 반복
    print(a)

#무한루프에서 ctrl + c 하면 실행중지 (=keyboard interrupt)

