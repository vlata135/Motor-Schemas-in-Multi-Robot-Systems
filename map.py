import math
import numpy as np
class MAP:
    def __init__(self, width, height,num_points,radius=200):
        self.width = width
        self.height = height
        self.center = (self.width // 2, self.height // 2)
        self.radius = radius
        self.num_points = num_points
        self.points = np.array(self.initial_pos())
        self.target_points = np.array(self.target_point())

    def calculate_initial_point_on_circle(self,angle):
        x = self.center[0] + self.radius * math.cos(angle)
        y = self.center[1] + self.radius * math.sin(angle)
        return (int(x), int(y))
    
    def initial_pos(self):
        points = []
        for i in range(self.num_points):
            angle = 2 * math.pi * i / self.num_points + math.pi / 6
            point = np.array(self.calculate_initial_point_on_circle(angle))
            points.append(point)
        return points
    
    def target_point(self):
        target_points = []
        for point in self.points:
            symmetric_point = (2*self.center[0] - point[0], 2*self.center[1] - point[1])
            target_points.append(symmetric_point)
        return target_points
        