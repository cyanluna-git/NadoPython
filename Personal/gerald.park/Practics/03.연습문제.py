# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
num = 0
sum = 0
while(num != 1000):
    num = num + 1
    if num % 3 == 0:
        sum = sum + num
        print(sum)
print(sum) 

# while 문을 이용해 * 탑
num = 0 
while(num != 6):
    print('*' * num)
    num += 1

# for 문으로 0~100 
for num in range (1,101):
    print(num)

# 4 
aClass = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for var in aClass:
    sum += var
avg = sum/ len(aClass)
print('학급점수총합 : {0}, 학생수 {1}, 평균,{2}'.format(sum,len(aClass),avg))

#5 리스트 내포 

# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# print(result)  

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)    