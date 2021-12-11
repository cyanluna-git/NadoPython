# 1부터 주어진 범위까지의 자연수중 소수를 판별해 주는 함수(is_prime)를 작성한 뒤 소수만 prime_numbers 라는 이름의 리스트에 담아보자. 
import time


def is_prime(number):
    primelist = [True] * number # 1부터 number 크기만큼의 True 리스트 선언
    n = int(number**0.5)   # 검색에 사용할 최대 소수는 sqrt(number) 보다 작거나 같다
    print(primelist)

    for i in range(2,n+1):  # 2부터 최대 소수 범위까지만 탐색 시작
        if primelist[i] == True:    # 리스트가 True 이면 i를 소수로 인식
            for j in range(i+i, number,i):  # 1~number 범위에서 소수 i의 배수들을 검색
                primelist[j] = False    # 소수 i의 배수들을 False 로 변경, 소수가 아니므로 리스트에서 제외
    
    prime_numbers=[]
    for prime in range(2,number):
        if primelist[prime]==True:
            prime_numbers.append(prime)

    return prime_numbers

number = int(input('범위를 입력하세요 : '))
start_time = time.time()
print('1부터 {0}까지 소수들의 집합 : {1}'.format(number,is_prime(number)))
print('소요시간: {0}초'.format(time.time() - start_time))


