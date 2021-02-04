# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
#
# name = "마린"
# hp = 40  # 체력
# damage = 5  # 공격력
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
#         name, location, damage))
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


# __init__ 은 생성자이다. 마린이나 탱크와 같이 클래스로부터 만드러지는 것들을 객체라 하고, 마린과 탱크는 인스턴스라고 한다.
# 객체가 생성될 때는 self를 제외하고 동일한 개수만큼 값을 던져줘야 한다.
# 멤버 변수는 self.name, self.hp 이런 것들이다. 클래스 내에서 정의된 변수이다.
# 이 변수를 가지고 초기화도 가능하고 사용도 할 수 있는 것이다.

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("\n유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))