import pygame
import numpy as np
from apf import * 
from robot import *
from map import *
import math

class DRAW:
    def __init__(self,num_robots):
        self.width = 800
        self.height = 600
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Robot Avoidance")
        self.num_robots = num_robots
        self.center = (self.width // 2, self.height // 2)
    
    def plot(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)

        map = MAP(self.width,self.height,self.num_robots,radius=240)
        initial_pos = map.points
        target_pos = map.target_points
        robots = []

        for i in range(self.num_robots):
            robot = ROBOT(target_pos[i],initial_pos[i])
            robots.append(robot)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill(WHITE)

            # Vẽ đường tròn
            pygame.draw.circle(self.screen, BLACK, self.center, 240, 2)

            for robot in robots:
                apf = APF(robot, robots)
                attr_force = apf.getAttractiveForce()
                rep_force = apf.getRepulsiveForce()
                net_force = attr_force + rep_force
                robot.velocity = net_force
                robot.updatePose()
                self.draw_robot(robot)
                
            pygame.display.flip()
            self.clock.tick(120)

        pygame.quit()

    def draw_robot(self,robot):
        pygame.draw.circle(self.screen, robot.color, (int(robot.current_pos[0]), int(robot.current_pos[1])), 10)
        for i in range(len(robot.trace)):
            pygame.draw.circle(self.screen, (255,215,0), (int(robot.trace[i][0]), int(robot.trace[i][1])), 2)
            if i > 0:
                pygame.draw.line(self.screen, (255,215,0), (int(robot.trace[i][0]), int(robot.trace[i][1])), (int(robot.trace[i-1][0]), int(robot.trace[i-1][1])), 2)

# if __name__ == "__main__":
#     draw = DRAW(10)
#     draw.plot()
    

    