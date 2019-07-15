old_position = 100
old_velocity = 0
old_fuel = 100
gravity = -10

while old_fuel >=0:
    if old_position > 0:
        thrusters = input("Set thrusters(0-20)")
        old_fuel = old_fuel - thrusters
        acceleration = gravity + thrusters
        old_position = old_position + old_velocity + acceleration * 0.5
        old_velocity = old_velocity + acceleration
        print(old_position, old_velocity, old_fuel)

        if old_position <= 0 and old_velocity >= - 3:
            print("Landing successful")
            break
        elif old_position <=0 and old_velocity <= -3:
            print ("Fall")
            break
        elif old_position >= 0 and old_fuel <= 0:
            print ("Free fall")
            break