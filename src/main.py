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
left_motor_2 = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
right_motor = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
right_motor_2 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
intake = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False)
clamp = DigitalOut(brain.three_wire_port.a)

try:

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
    brain.screen.print("\n Running auton.. Currently on function driveDistance with args " + amount.str() + speed.str())
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
    brain.screen.print("\n Running auton.. Currently on function rotate with args " + amount.str() + speed.str())
    left_motor.set_velocity(speed, PERCENT) 
    right_motor.set_velocity(speed, PERCENT)
    left_motor_2.set_velocity(speed, PERCENT) 
    right_motor_2.set_velocity(speed, PERCENT) 
    
    #  do not move left_motor
    right_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees * -1, DEGREES, False) 
    left_motor.spin_for(FORWARD, amount / 360 * turnCirc * inches2Degrees  , DEGREES) 


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
      print("Hello!")
  def autonomous():
      brain.screen.clear_screen()
      brain.screen.print("In the wise words of the class of 2033: \nRizz Sigma Skibidi Gyatt \n")
      intake.spin_for(FORWARD, 1, TURNS, 75, RPM)
      turnRight(360, 100)
      driveDist(42, 65)
      intake.spin_for(FORWARD, 3, TURNS, 75, RPM)
      rotateLeft(90, 65)
      driveDist(20, 70)
      rotateRight(180, 70)
      clamp.set(extended)
      driveDist(-6, 70)
      clamp.set(retracted)
      intake.spin_for(FORWARD, 15, TURNS, 100, RPM)


  # Main Controller loop to set motors to controller axis postiions
  def user_control():
      while True:
          lmotorvel = controller_1.axis3.position()
          rmotorvel = controller_1.axis2.position()
          left_motor.set_velocity(lmotorvel, PERCENT)
          left_motor_2.set_velocity(lmotorvel, PERCENT)
          right_motor.set_velocity(lmotorvel, PERCENT)
          right_motor_2.set_velocity(lmotorvel, PERCENT)

          left_motor.spin(FORWARD)
          left_motor_2.spin(FORWARD)
          right_motor.spin(FORWARD)
          right_motor_2.spin(FORWARD)

          brain.screen.print_at("4886A", x=50, y=50)
          brain.screen.print_at(str(lmotorvel) + ", " + str(rmotorvel), x=50, y=85)
          
          if controller_1.buttonA.pressing:
              intake.spin(FORWARD)
          elif controller_1.buttonB.pressing:
              intake.spin(REVERSE)
          elif controller_1.buttonX:
            if clamp.value:
              clamp.set(retracted)
            else:
              clamp.set(extended)
          else: return
          wait(20, MSEC)



      #wait(20, MSEC)
except:
  brain.screen.print("An error happened :(")
