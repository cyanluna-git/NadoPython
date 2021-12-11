# # 8-1. 표준입출력
# import sys
# print("Python", "Java", file=sys.stdout) # 표준출력
# print("Python", "Java", file=sys.stderr) # 표준 에러처리

# # 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # 오른쪽 정렬, 왼쪽 정렬 : 숫자는 str로 변환 필요 


# # 은행 대기순번표
# # 001, 002, 003, ...
# for num in range(1, 21): # 1~20까지 숫자
#     print("대기번호 : " + str(num).zfill(3)) #숫자 앞에 0으로 채우기

# answer = input("아무 값이나 입력하세요 : ") # 사용자 입력은 항상 문자형으로 저장
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")