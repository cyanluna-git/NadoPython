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

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 두 개의 부모 클래스를 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 드랍쉽 : 공중 유닛, 수송기

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")