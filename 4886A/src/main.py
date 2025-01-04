# ----------------------------------------------------------------------------- #
#                                                                               #                                                                          
#    Project:        4886A                                                      #
#    Module:         main.py                                                    #
#    Author:         Connor Abraham & Ira Corbett                               #
#    Created:        September 3rd 2024                                         #
#    Description:    4886A code                                                 #       
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
from vex import * # type: ignore
 


# Brain should be defined by default
brain=Brain() # type: ignore


# Robot configuration code
controller_1 = Controller(PRIMARY) # type: ignore
left_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True) # type: ignore
left_motor_2 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True) # type: ignore
right_motor = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False) # type: ignore
right_motor_2 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False) # type: ignore 
intake = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False) # type: ignore
in2 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True) # type: ignore
clamp = DigitalOut(brain.three_wire_port.a) # type: ignore
#corner_sweeper = DigitalOut(brain.three_wire_port.b)
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
clampbutton = 0

# Auton steps

def driveDist(amount, speed): 
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT) 
  amount *= inches2Degrees
  left_motor.spin_for(FORWARD, amount, DEGREES, wait=False) #false
  right_motor.spin_for(FORWARD, amount, DEGREES, wait=False) #false
  left_motor_2.spin_for(FORWARD, amount, DEGREES, wait=True)#true
  right_motor_2.spin_for(FORWARD, amount, DEGREES, wait=True) #true


def rotateLeft(amount, speed):
  brain.screen.print("\n Running auton.. Currently on function rotate with args " + amount.str() + speed.str())
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT)
  
  #  do not move right_motor
  left_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees  * -1, DEGREES, False)
  left_motor_2.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees * -1, DEGREES, False)

def rotateRight(amount, speed):
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT)
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT) 
  
  #  do not move left_motor
  right_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees * -1, DEGREES, False) 
  right_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees * -1, DEGREES, False)

def turnLeft(amount, speed):
  brain.screen.print("\n Running auton.. Currently on function rotate with args " + amount.str() + speed.str())
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT) 
  
  #  do not move left_motor
  right_motor.set_velocity(speed, PERCENT) 
  right_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees, DEGREES, False) 

def turnRight(amount, speed):
  brain.screen.print("\n Running auton.. Currently on function rotate with args " + amount.str() + speed.str())
  left_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  right_motor.set_velocity(speed, PERCENT) 
  left_motor_2.set_velocity(speed, PERCENT) 
  right_motor_2.set_velocity(speed, PERCENT)
  #  do not move right_motor
  left_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees, DEGREES, False) 
# GitHub test



# Begin project code

def pre_auton():
    brain.screen.print("Hello")



def autonomous():
  clamp.set(extended)
  driveDist(-10, 50)
  clamp.set(retracted)
  intake.spin_for(FORWARD, 5, TURNS, 100, RPM)
#4.5 rotations

# skills auton code
#def skills_autonomous():
  #print("SKILLS AUTONOMOUS MODE")
  #clamp.set(extended)
  #driveDist(1.5, 70)
  #rotateRight(90, 50)
  #driveDist(-3, 70)
  #clamp.set(retracted)
  #rotateRight(180, 50)
  #intake.spin_for(FORWARD, 7, TURNS, 100, RPM)
  #driveDist(2.0625, 70)
  #driveDist(0.6875, 70)
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
    clamp.set(False)
    brain.screen.clear_screen()
    brain.screen.print("USER CONTROL")

    while True:

        if arcade == True:
          # Tank drive is "Cringe", as the kids say.
#          lmotorvel = controller_1.axis3.position() / 1.5
#          rmotorvel = controller_1.axis2.position() / 1.5
#          left_motor.set_velocity(lmotorvel, PERCENT)
#          left_motor_2.set_velocity(lmotorvel, PERCENT)
#          right_motor.set_velocity(rmotorvel, PERCENT)
 #         right_motor_2.set_velocity(rmotorvel, PERCENT)
#       else:
          # Arcade drive is "Sigma", as the kids say.
          lmotorvel = (controller_1.axis3.position() + controller_1.axis4.position())
          rmotorvel = (controller_1.axis3.position() - controller_1.axis4.position())
          left_motor.set_velocity(lmotorvel, PERCENT)
          left_motor_2.set_velocity(lmotorvel, PERCENT)
          right_motor.set_velocity(rmotorvel, PERCENT)
          right_motor_2.set_velocity(rmotorvel, PERCENT)

        # Run intake (forward)
        if controller_1.buttonA.pressing():
            intake.set_velocity(-105, RPM)
            in2.set_velocity(-110, RPM)
        # Extake????
        elif controller_1.buttonB.pressing():
            intake.set_velocity(90, RPM)
            in2.set_velocity(200, RPM)
        # Cease0
        else:
           intake.set_velocity(0, RPM)
           in2.set_velocity(0, RPM)

        # Mobilegoal clamp
        if controller_1.buttonX.pressing():
           if clampbutton == 0:
            clampbutton = 1
            if clamp.value() == 0:
              brain.screen.clear_line(1)
              brain.screen.set_cursor(1,1)
              brain.screen.print("Clamp = true")
              clamp.set(True)
            elif clamp.value() == 1:
              brain.screen.clear_line(1)
              brain.screen.set_cursor(1,1)
              brain.screen.print("Clamp = false")
              clamp.set(False)
        else: 
          clampbutton = 0
        #corner sweeper
 #       if controller_1.buttonR1.pressing():                                                 
 #           if corner_extend == 0:
 #             corner_extend = 1
  #            if corner_sweeper.value() == 0:
  #              corner_sweeper.set(True)
   #           elif corner_sweeper.value() == 1:
   #             corner_sweeper.set(False)
   #    else:
  #        corner_extend = 0
        # Activate or deactivate the garbage drive mode
        brain.screen.print_at("4886A", x=50, y=50)
        brain.screen.print_at(str(lmotorvel) + ", " + str(rmotorvel), x=50, y=85)
        
        wait(20, MSEC)



    #wait(20, MSEC)
# Don't delete this one anymore
comp = Competition(user_control, autonomous)
# Or this one
pre_auton()