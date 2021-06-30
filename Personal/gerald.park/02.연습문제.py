# 1. 홍길동씨 평균점수 

# eng = 80
# kor = 75
# mat = 55
# avg = (eng + kor + mat)/3

# scores = [80,75,55]
# total = sum(scores)
# avg = total / len(scores)
# print("평균점수 : {0}".format(avg))

# 2. 13이 홀짝? 
# num = 13
# rad = num % 2
# if rad == 1:
#     print ('{0}은 홀수 입니다.'.format(num))
# else:
#     print ('{0}은 짝수 입니다.'.format(num))

# 3.주민번호 슬라이싱 
# jumin = '881120-1068234'
# jumin_split = jumin.split('-')
# yymmdd = jumin_split[0]
# idnumber = jumin_split[1]

# 4. 주민번호 보고 남자 여자? 
# 문자 '1' 과 숫자 1 은 다르다! 
# jumin = '881120-1068234'
# gender = jumin[7]
# if gender == '1': 
#     print('남자')
# elif gender == '2': 
#     print('여자')

# 5. replacing 
# a = "a:b:c:d"
# a = a.replace(':','#')
# print(a)

# 6. sort 
# Quick Sort Bubble Sort 몰라도 된다. 
# a = [1,3,5,4,2]
# a.sort(reverse=True)
# print(a)

# 7. list join
# message = ['life', 'is', 'too', 'short']
# print(message)
# print(' '.join(message))

# 11.  a 리스트에 중복 숫자를 제거하기
# a = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5]
# s = set(a)
# print(s)

# 12. reference 
a = b = [1, 2, 3]
a[1] = 4
print(b)