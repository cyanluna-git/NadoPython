# startcraft 9-10, 11
from random import *

# class 예시 시작
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        # self.damage = damage
        # print("{0} 유닛이 생성 되었습니다.".format(self.name) )
        # print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크", 150, 35)


# __init__ 생성자 클래스 객체 동일한 변수를 입력해야됨

# 멤버 변수

# 레이스
# wraith1 = Unit("레이스",80,5)
# print(wraith1.hp, wraith1.name)             # 멤버 변수를 외부에서도 사용가능하다]

# wraith2 = Unit("빼앗은 유닛",80,5)
# wraith2.clocking = True    # *******외부에서 객체의 멤버 변수를 확장할 수 있음 기존 객체에는 해당 내용 반영 없음

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 공격 유닛
class AttackUnit(Unit):  # 공격 유닛은 유닛을 상속받아서 사용됨
    def __init__(self, name, hp, speed, damage):
        # self.name = name
        # self.hp = hp
        # 유닛 상속
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
              .format(self.name, location, self.damage))


# 파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중 상속
# 부모 클래스를 2개 이상 상속 받는 경우에?

# 드랍쉽 공격은 불가함
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
              .format(name, location, self.flying_speed))


# 다중상속됨
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드느 0으로 출력
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # 연산자 오버로딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# valkyrie = FlyableAttackUnit("발키리", 200, 6,5)
# valkyrie.fly(valkyrie.name,"3시")

# 연산자 오버로딩 // 부모클래스에서 선언된 내용을 자식 클래스에서 변경하여 사용 오버로딩'

#
# #벌쳐
# Vulture = AttackUnit("벌쳐",80,10, 20)
# #배틀크루저
# battlecruiser = FlyableAttackUnit("배틀크루저",500, 25, 3)
#
# Vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")             # 지상, 공중 유닛을 구분하여서 move fly를 사용해야됨
#
# # 연산자 오버로딩//fly --> move
# battlecruiser.move("11시")


# ****Pass****

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self,name,hp,0)
#         super().__init__(name, hp,0)    # self를 입력하지 않아도됨, 다중 상속시에는 문제가 됨 / 최우선 상속 클래스만 지칭 가능함 / 모든 부모 클래스에 대한 초기화가 필요할 경우 명시적으로 표기해줘야됨
#         # pass            # 정의된 내용을 완성하지 않고 미리 작업을 추가함?

# # 서플라이 디폿
# supply_depot = BuildingUnit("서플라이",500, "7시")

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드
    seize_developed = False  # 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 시즈모드 X
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 시즈모드 O -> 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 해제 상태

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = True


def game_strat():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")



# 실제 게임 진행
game_strat()

# 마린 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 생성
t1 = Tank()
t2 = Tank()

# 레이스 생성
w1 = Wraith()

# 유닛 일괄 관리      리스트에 추가해서 관리  생선된 모든 유닛 append
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("탱크 시즈 모드 개발 완료")

# 공격 모드 준비 (마린 스팀팩, 탱크 시즈 레이스)
for unit in attack_units:
    if isinstance(unit, Marine):             # 객체를 구분 / 지금 만들어진 객체가 어떤 클래스 인지를 확인하기 위함
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


# 전국 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤

# 게임종료
game_over()

# # ***************************종료************************
#
#
#
# # Quiz 8 주어진 코드를 활용하여 부동산 프로그램을 작성하시오
#
# # (출력 예제)
# # 총 3대의 매물이 있습니다.
# # 강남 아파트 매매 10억 2010년
# # 마포 오피스텔 전세 5억 2007년
# # 송파 빌라 월세 500/50 2000년
#
# # [코드]
# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#
#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type \
#               , self.price, self.completion_year)
#
# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")
#
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)
#
# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()