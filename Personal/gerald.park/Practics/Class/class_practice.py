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