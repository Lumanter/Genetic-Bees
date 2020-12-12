from Tree import *
from math import cos, sin, radians, degrees
import bisect


def get_coordinates_around_center( angle, distance,starting_point):
        """ Returns the x,y coordinates around the sonar center from a given angle and distance.

            Args:
                angle (float): Rotation value from the sonar perspective .
                distance (int): Distance from the sonar to the coordinates.

            Returns:
                :obj:`list` of float: Tuple of coordinates.
        """
        center = starting_point
        point = Point(center.x+distance, center.y) # initial point to rotate
        x = center.x + cos(angle) * (point.x - center.x) - sin(angle) * (point.y - center.y)
        y = center.x + sin(angle) * (point.x - center.x) + cos(angle) * (point.y - center.y)
        return x, y


def get_bee_path_area(direction,deflection,starting_point,distance):
    left_angle = direction - (deflection)
    left_angle = (left_angle + 360) if (left_angle < 0) else left_angle  # adjust over 360 angle
    right_angle = direction + (deflection)
    right_angle = (right_angle - 360) if (right_angle > 360) else right_angle # adjust negative angle
    
    left_point = get_coordinates_around_center(left_angle,distance,starting_point)
    right_point = get_coordinates_around_center(right_angle,distance,starting_point)

    area=Area([Point(right_point[0],right_point[1]),Point(left_point[0],left_point[1]),starting_point])
    return area


def get_flowers_in_the_area(area,flowers):
    flowers_in_the_area=[]
    for i in range(len(flowers)):
        point=Point(flowers[i].x,flowers[i].y)    
        if area.contains(point):
            flowers_in_the_area.append(flowers[i])
    return flowers_in_the_area


def set_flower_point_distance(flowers,starting_point):
    flows=[]
    distances=[]
    for i in range(len(flowers)):
        point=Point(flowers[i].x,flowers[i].y)
        d=point.get_distance_to(starting_point)
        
        position = bisect.bisect(distances, d)
        bisect.insort(distances, d)
        flows.insert(position,flowers[i])
    
    return flows



