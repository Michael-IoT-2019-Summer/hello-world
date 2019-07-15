#-*-coding:utf-8 -*-

old_position = 100
old_velocity = 0
old_fuel = 100
gravity = -10

# thrusters = input('숫자를 입력하세요: ')

# def new_fuel(old_fuel, thrusters):
#     old_fuel = old_fuel - thrusters
#     return old_fuel
#
# def acceleration(gravity, thrusters):
#     acceleration = gravity + thrusters
#     return acceleration
#
# def new_position(old_position, old_velocity, acceleration):
#     old_position = old_position + old_velocity + acceleration * 0.5
#     return old_position
#
# def new_velocity(old_velocity, acceleration):
#     old_velocity = old_velocity + acceleration


print(old_position, old_velocity, old_fuel )

while old_fuel > 0:
    thrusters = input("Set thrusters(0-20)")
    # old_fuel = new_fuel(old_velocity, thrusters)
    # old_velocity  = new_velocity(old_velocity, acceleration)
    # old_position = new_position(old_position, old_velocity, acceleration)
    old_fuel = old_fuel - thrusters
    acceleration = gravity + thrusters
    old_velocity = old_velocity + acceleration
    old_position = old_position + old_velocity + acceleration * 0.5
    print(old_position, old_velocity, old_fuel)

if old_fuel > 0:
    if old_position <= 0:
        print("good")
    else:
        print("bad")