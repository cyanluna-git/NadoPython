# # for 구문 # #
# starbucks = ["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다." .format(customer))

#while 구문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요." .format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")