# class Unit:
#     def __init__(self, name, hp, damage): # 생성자
#         self.name = name # 멤버 변수
#         self.hp = hp # 멤버 변수
#         self.damage = damage # 멤버 변수
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 멤버 변수를 외부에서 접근 가능


# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은레이스", 80, 5)
# wraith2.clocking = True # 객체에 외부에서 변수를 추가 할당 가능
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))