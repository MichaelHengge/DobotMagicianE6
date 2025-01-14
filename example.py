import time
from DobotTCP import Dobot, FlexGripper

robot = Dobot()
gripper = FlexGripper(robot)
robot.Connect()
robot.EnableRobot()
gripper.open()
time.sleep(3)
gripper.close()