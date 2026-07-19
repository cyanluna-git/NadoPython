# 메소드 오버라이딩

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # 생성자
        self.name = name # 멤버 변수
        self.hp = hp # 멤버 변수
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛 : 일반 유닛으로부터 상속        
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # 생성자
        Unit.__init__(self, name, hp, speed) # Unit 에서 선언한 init 부분을 호출
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
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): # 두 개의 부모 클래스를 다중 상속
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

# # 벌쳐
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")

# 위와 같이 하면 지상인지 공중인지 일일히 파악해서 move 또는 fly 써야함
# 이를 해결하기 위해 오버라이딩 적용
# FlyableAttackUnit 에 새로운 함수를 오버라이딩


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 두 개의 부모 클래스를 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")
