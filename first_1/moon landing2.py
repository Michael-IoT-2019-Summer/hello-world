#-*-coding:utf-8 -*-

old_position = 100
old_velocity = 0
old_fuel = 100
gravity = -10

print(old_position, old_velocity, old_fuel )

#조건 3가지 성공했을때, 땅에 도착했는데 속도가 3이하, 추락은 : 땅에 떨어졌는데 속도가 3이상, free fall 땅에 도착하지 않았는데 연료가 떨어진경우
while old_fuel >=0:
    if old_position > 0:
        thrusters = input("Set thrusters(0-20)")
        old_fuel = old_fuel - thrusters
        acceleration = gravity + thrusters
        old_position = old_position + old_velocity + acceleration * 0.5
        old_velocity = old_velocity + acceleration
        print(old_position, old_velocity, old_fuel)

    elif old_position <=0 and old_velocity <= 3:
        print("Landing successful")
        break

    elif old_position >0 and old_velocity >= 3:
        print("Fail")
        break

    elif old_position >0 and old_fuel <= 0:
        print("Free fall")
        break

    # else:
    #     if old_fuel >= 0:
    #         print("Landing successful")
    #         break
    #
    #     else:
    #         print ("Landing fail")
    #         break




