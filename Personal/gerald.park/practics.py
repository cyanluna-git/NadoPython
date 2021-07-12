# kor = 80
# eng = 75
# mat = 55
# sos = 55
# total_score = kor + eng + mat
# avg_score = total_score / 4
# print('평균점수 : {0} 합계 {1}'.format(avg_score, total_score))

# scores = [80, 75, 55, 45]
# total = 0
# for var in scores:
#     total = total + var
# avg = total/len(scores)
# print('평균점수 : {0} 합계 {1}'.format(avg, total))

# scores = [80, 75, 55, 45, 90, 42]
# total = sum(scores)
# avg = total/len(scores)
# print('평균점수 : {0} 합계 {1}'.format(avg, total))

# var = 13
# rad = var % 2
# if rad == 0:
#     print("{0}는 짝수입니다".format(var))
# else:
#     print("{0}는 홀수입니다".format(var))


# Q3 
# jumin = '881120-1068234'
# yymmdd = jumin.split('-')[0]
# idnum = jumin.split('-')[1]
# print(yymmdd[0:2])
# print(jumin[7])

# Q5
# a = 'a:b:c:d'
# a = a.replace(':','#')
# print(a)

# Q6
# a = [1 ,3, 5, 4, 2]
# a.sort(reverse = True)
# print(a)

# Q7
# a = ['Life', 'is', 'too', 'short']
# print('.'.join(a))

# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# a = set(a)
# print(a)

a = [1, 2, 3]
a = b = [1, 2, 3]
a[1] = 4 
print(b)
