# 1부터 주어진 범위까지의 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성한뒤 홀수만 odd_numbers 라는 이름의 리스트에 담아보자. 

def is_odd(number):
    return number%2 == 1

max_number = int(input('범위를 입력하세요 : '))
numbers = range(1 , max_number+1)
odd_numbers = []

for number in numbers:
    if is_odd(number): 
        print('숫자 : {0}은 홀수 입니다.'.format(number))
        odd_numbers.append(number)
print(odd_numbers)

# 숙제 
# 1부터 주어진 범위까지의 자연수가 소수인지 판별해 주는 함수(is_prime)를 작성한뒤 홀수만 prime_numbers 라는 이름의 리스트에 담아보자. 

# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def average(numbers):
    return sum(numbers)/len(numbers)

print(average(numbers))