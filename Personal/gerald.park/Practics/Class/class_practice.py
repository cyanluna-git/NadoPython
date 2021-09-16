# # 마린 : 공격 유닛, 군인 , 총을 쏠수 있음 
# name = "마린"
# hp = 40
# damage = 5

# print("{0}유닛이 생성 되었습니다.".format(name))
# print("체력 {0}, 공격력 {1} \n".format(hp, damage))

# #탱그, 공격 유닛, 탱크,포르 ㄹ쏠수 있음, 일반모드/시즈모드

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성 되었습니다".format(tank_name))
# print("체력{0}, 공격력{1}\n ".format(tank_hp, tank_damage))

# def attach(name, location, damage):
#     print("체력 : {0}: 공격력 {1} 시 방향으로 공격합니다. ")

class Unit:
    def __init__(self,name, hp, damage):  
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("마린",150,35)


# 레이스 : 공중유닛, 비행기, 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 {1} ".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것 ( 빼앗음 )
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # 클래스 외부에서 클로킹 속성을 추가 해버림 이것은 wrath2 object 에서만 적용이 됨 . 

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))


# 공격유닛 

class AttackUnit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp 
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다 [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage): 
        print("{0}:{1} 데지미를 입었습니다.".format(self.name,  damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}.".format(self.name,  self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50 ,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)