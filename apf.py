import numpy as np
from robot import *
import numpy as np

class APF:
    def __init__(self,robot, robots, att_factor=1.0, rep_factor=1.0,att_d_star=1.0,rep_q_star=1.0):
        # self.goal = goal
        self.robots = robots 
        self.robot = robot
        
    def getAttractiveForce(self):
        return 0.006 * (self.robot.target_pos - self.robot.current_pos)

    def getRepulsiveForce(self):
        f = np.zeros(2)
        for rob in self.robots:
            if rob == self.robot:
                continue
            rho = np.linalg.norm(self.robot.current_pos - rob.current_pos)
            if rho < 60:
                f += 0.4 * (60 -rho)/(60-30) * (self.robot.current_pos - rob.current_pos)
            else:
                f += 0.0
        return f

    