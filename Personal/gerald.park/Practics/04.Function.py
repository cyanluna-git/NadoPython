# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance + money))
#     return balance + money


# def withdraw(balance, money):
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#             print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))

# def  withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission
    

# balance = 0 # 잔액 
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 600)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commission,balance))


# Function 2 
# def prifile(name, age, main_lang):
#     print("이름 {0}\t나이: {1}\t주 사용언어: {2})" \
#         .format(name,age,main_lang)

# def prifile(name, age=17, main_lang="Python"):
#     print("이름 {0}\t나이: {1}\t주 사용언어: {2})" \
#         .format(name, age, main_lang)

# prifile("유재석")
# prifile("김태호")

# 넘겨주는 인자 순서가 바뀌어도 됨. 
# profile(name="유재석", main_lang="jave", age = 29)

# 가변인자
# def profile(name, age, *language):
#     print("이름 : {0}\t, 나이: {1} \t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C","C++","C#")
# profile("김태호", 26, "Kotlin", "swift")

# 전역변수 사용 
gun = 10
# def checkpoint(soldiers):
#     global gun # 전역공간에 있는 gub 을 사용함. 
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수내] 남은 총: {0}".format(gun))
    return gun

gun = checkpoint_ret(gun, 2)