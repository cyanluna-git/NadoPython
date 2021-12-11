class Unit:
    def __init__(self, name, hp, damage): # 생성자
        self.name = name # 멤버 변수
        self.hp = hp # 멤버 변수
        self.damage = damage # 멤버 변수
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage): # 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # location 은 전달받은 값을 사용

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
