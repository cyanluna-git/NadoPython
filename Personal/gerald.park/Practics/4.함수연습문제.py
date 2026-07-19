# 1부터 주어진 범위까지의 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성한뒤 홀수만 odd_numbers 라는 이름의 리스트에 담아보자. 

def is_odd(number):
    return number%2 == 1

max_number = int(input('범위를 입력하세요 : ')) # input 으로 받으면 기본 string이므로 int 숫자형으로 변환해줘야한다. 
numbers = range(1 , max_number+1)
odd_numbers = []
for number in numbers:
    if is_odd(number):         
        odd_numbers.append(number)
print('1부터 {0}까지 홀수들의 집합 : {1}'.format(max_number,odd_numbers))

# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def average(numbers):
    return sum(numbers)/len(numbers)

print('주어진 리스트 평균값은 : {0}, 요소의 개수 : {1}'.format(average(numbers),len(numbers)))

# 숙제1 : # 1부터 주어진 범위까지의 자연수가 소수인지 판별해 주는 함수(is_prime)를 작성한뒤 홀수만 prime_numbers 라는 이름의 리스트에 담아보자. ! 
# 숙제2 : prime_number를 구하는데 소요되는 시간을 측정해보자! (100까지 소수를 구하는데 소요시간, 1000까지소수를 구하는데 소요시간. 100000000은??)