# a = "Life is too short, you need python"

# if "wife" in a: print("wife") # FALSE 
# elif "python" in a and "you" not in a: print("python") #FASLE = TRUE FALSE 
# elif "shirt" not in a: print("shirt") # TRUE
# elif "need" in a: print("need")
# else: print("none")

# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

# num = 0
# sum = 0
# while(num < 1001):
#     num += 1
#     if num % 3 == 0:
#         sum += num
#         print(sum)

# Q3 

# star = 0
# while(star < 10):
#     star += 1 
#     print('*' * star)


# alist = [1,2,3,4,...100]
# num = 0
# while(num < 100):
#     num += 1
#     alist.append(num)
# for a in alist:
#     print(a)

# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

# aClass = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100, 54]
# sum = 0
# for score in aClass:
#     sum += score
# avg = sum / len(aClass)
# print('학급전체점수:{0}, 학급원{1}, 평균점수:{2}'.format(sum,len(aClass),avg))

# 리스트 내포(list comprehension)
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)


