# print("python", "Java","javascript", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "Java","javascript", file=sys.stdout)
# print("python", "Java","javascript", file=sys.stderr)

score = {"수학":0, "영어":50, "코딩":100}
for subject, score in score.items():
    print(subject.ljust(8),str(score).rjust(4), sep=":")

# 은행 대기 순번표
# 001, 002, 003
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))

# 오...신기하네요.. ~ 
# 따라하고 계시리라 믿습니다 ~~ 

# answer = input("아무값이 나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 "+ answer+"입니다.")

# input으로 입력을 받으면 항상 string 으로 받는다. 