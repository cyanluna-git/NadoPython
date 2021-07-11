#숫자형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자열
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#Boolean 참/거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

#변수 (애완동물을 소개해 주세요~)

animal = "고양이"
name = "해피"
age = 2
hobby = "공놀이"
is_adult = age >=3

print("우리집 "+animal+"의 이름은 "+name+"예요")
#+를 이용하기 OR 사용안하는 방법
print(name+"는 " +str(age)+"살이며, "+hobby+"을 매우 좋아해요.")
print(name,"는", age, "살이며, " ,hobby, "을 아주 좋아해요.")
print(name,"는 어른일까요? "+str(is_adult))


#주석처리 방법
''' 이렇게
하면 
여러문장이
주석처리가 됩니다.'''

#하고 싶은 문장 드래그 후 Crtl+/ 하면 전체 문장이 주석처리됨. 해지는 반대 방법으로 하면됨.
print("")
print("Quiz 변수를 이용하여 다음 문장을 출력하시오.")

station1 = "사당"
station2 = "신도림"
station3 = "인천공항"

print(station1,"행 열차가 들어오고 있습니다.")
print(station2,"행 열차가 들어오고 있습니다.")
print(station3,"행 열차가 들어오고 있습니다.")