#문자열 연산하기
#문자열 더하기
head="Python"
tail=" is fun!"
print(head+tail)

#문자열 곱하기
print("="*50)
print("My program")
print("="*50)

#문자열 길이 구하기

#1. 인덱싱

a="Life is too short, you need Python"
print(a[3]) #e
print(a[-1]) #n
print(a[-5]) #y
print(a[0:4]) #슬라이싱 기법1
print(a[19:-7]) #슬라이싱 기법2

#2. 슬라이싱 활용하기
a="20210615Rainy"
year=a[:4]
day=a[4:8]
weather=a[8:]
print(year)
print(day)
print(weather)

#3. 연습문제
#Q1
a=80
b=75
c=55
average=(a+b+c)/3
print("홍길동의 평균점수는 " ,average, "입니다.")

#Q2 : 13이 짝수인지 홀수인지 알아보기
print(13%2)

#Q3홍길동의 주민번호
Ident="881120-1068234"
year=Ident[:2]
month=Ident[2:4]
day=Ident[4:6]
left=Ident[7:]
print(year)
print(month)
print(day)
print(left)