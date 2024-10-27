# ----------------------------------------------------------------------------- #
#                                                                               #                                                                          
#    Project:        Tankdrive Test                                             #
#    Module:         main.py                                                    #
#    Author:         Connor Abraham                                             #
#    Created:        September 3rd 2024                                         #
#    Description:    This example will use Controller button events to          # 
#                    control the V5 Clawbot arm and claw                        #
#                                                                               #                                                                          
#    Configuration:  V5 Clawbot (Individual Motors)                             #
#                    Controller                                                 #
#                    Claw Motor in Port 3                                       #
#                    Arm Motor in Port 8                                        #
#                    Left Motor in Port 1                                       #
#                    Right Motor in Port 10                                     #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()



# Robot configuration code
controller_1 = Controller(PRIMARY)
left_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
left_motor_2 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
right_motor = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
right_motor_2 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
intake = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False)
in2 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
clamp = DigitalOut(brain.three_wire_port.a)

# Constants

PI = 3.14159265

wheelDia = 3 # inches
wheelCirc = wheelDia*PI # Wheel circumference (in.)
motorGearT = 48
wheelGearT = 72
wheelWidth = 10 # robot width in inches
turnCirc = wheelWidth * (2*PI)
inches2Degrees = ((360/wheelCirc)*(wheelGearT/motorGearT))
extended = True
retracted = False

# Auton steps

def driveDist(amount, speed): 
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT) 
  left_motor.spin_for(FORWARD, amount * inches2Degrees, DEGREES, False) 
  right_motor.spin_for(FORWARD, amount * inches2Degrees, DEGREES) 
  left_motor_2.spin_for(FORWARD, amount * inches2Degrees, DEGREES, False) 
  right_motor_2.spin_for(FORWARD, amount * inches2Degrees, DEGREES) 


def rotateLeft(amount, speed):
  brain.screen.print("\n Running auton.. Currently on function rotate with args " + amount.str() + speed.str())
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT) 
  
  #  do not move right_motor
  right_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees, DEGREES, False) 
  left_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees  * -1, DEGREES) 


def rotateRight(amount, speed):
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT)
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT) 
  
  #  do not move left_motor
  right_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees * -1, DEGREES, False) 
  left_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees, DEGREES) 


def turnLeft(amount, speed):
  brain.screen.print("\n Running auton.. Currently on function rotate with args " + amount.str() + speed.str())
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT) 
  
  #  do not move left_motor
  right_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees, DEGREES) 

def turnRight(amount, speed):
  brain.screen.print("\n Running auton.. Currently on function rotate with args " + amount.str() + speed.str())
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT)
  #  do not move right_motor
  left_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees, DEGREES) 

# Begin project code

def pre_auton():
    brain.screen.print("Hello!")
def autonomous():
  driveDist(20, 65)
  rotateRight(180, 70)
  intake.spin_for(FORWARD, 15, TURNS, 100, RPM)


# Main Controller loop to set motors to controller axis postiions
def user_control():
    # Basic configuration
    left_motor.spin(FORWARD)
    left_motor_2.spin(FORWARD)
    right_motor.spin(FORWARD)
    right_motor_2.spin(FORWARD)
    intake.spin(FORWARD)
    in2.spin(FORWARD)
    lmotorvel = 0
    rmotorvel = 0
    arcade = True
    brain.screen.clear_screen()
    brain.screen.print("Please do not pet the robot \n boop beep.")

    while True:

        if arcade == False:
          # Tank drive is "Sigma", as the kids say.
          lmotorvel = controller_1.axis3.position() / 1.5
          rmotorvel = controller_1.axis2.position() / 1.5
          left_motor.set_velocity(lmotorvel, PERCENT)
          left_motor_2.set_velocity(lmotorvel, PERCENT)
          right_motor.set_velocity(rmotorvel, PERCENT)
          right_motor_2.set_velocity(rmotorvel, PERCENT)
        else:
          # Arcade drive is "Cringe", as the kids say.
          lmotorvel = (controller_1.axis3.position() + controller_1.axis4.position())
          rmotorvel = (controller_1.axis3.position() - controller_1.axis4.position())
          left_motor.set_velocity(lmotorvel, PERCENT)
          left_motor_2.set_velocity(lmotorvel, PERCENT)
          right_motor.set_velocity(rmotorvel, PERCENT)
          right_motor_2.set_velocity(rmotorvel, PERCENT)

        # Run intake (forward)
        if controller_1.buttonA.pressing():
            intake.set_velocity(85, RPM)
            in2.set_velocity(90, RPM)
        # Extake????
        elif controller_1.buttonB.pressing():
            intake.set_velocity(-85, RPM)
            in2.set_velocity(-90, RPM)
        # Cease
        else:
           intake.set_velocity(0, RPM)
           in2.set_velocity(0, RPM)

        # Mobilegoal clamp
        if controller_1.buttonX.pressing():
       #   if clamp.value:
          clamp.set(retracted)
        else:
          clamp.set(extended)
        # Activate or deactivate the garbage drive mode
        if controller_1.buttonL1.pressing():
          if arcade:
            arcade = False
          else:
            arcade = True
                   



        brain.screen.print_at("4886A", x=50, y=50)
        brain.screen.print_at(str(lmotorvel) + ", " + str(rmotorvel), x=50, y=85)
        

        
        wait(5, MSEC)



    #wait(20, MSEC)
# Don't delete this one anymore
comp = Competition(user_control, autonomous)
# Or this one
pre_auton()