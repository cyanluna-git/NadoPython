# 일반 유닛
class Unit:
    def __init__(self, name, hp): # 생성자
        self.name = name # 멤버 변수
        self.hp = hp # 멤버 변수

# 공격 유닛 : 일반 유닛으로부터 상속        
class AttackUnit(Unit):
    def __init__(self, name, hp, damage): # 생성자
        Unit.__init__(self, name, hp) # Unit 에서 선언한 init 부분을 호출
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
# 메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
