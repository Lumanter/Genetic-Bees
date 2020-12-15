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


def search_bees(bees, flowers, honeycomb_point=Point(64, 64)):
    b = []
    for bee in bees:
        # print("direccion: ",str(bee.get_fav_dir()))
        # print("desviacion: ",bee.deviation_angle)
        # print("distancia: ",bee.search_radius)
        # print("star point: ",bee.get_honeycomb_start())
        point = bee.get_honeycomb_start()
        point = Point(point[0], point[1])

        flowers_in_area = get_flowers_in_the_area(
            get_bee_path_area(bee.get_fav_dir(), bee.deviation_angle, honeycomb_point, bee.search_radius), flowers)

        if flowers_in_area:
            set_flower_point_distance(flowers_in_area, point)

            tree = Tree(visiting_a_node_chace)
            if flowers_in_area:
                for i in range(len(flowers_in_area)):
                    tree.insert(tree.root, flowers_in_area[i])

            if bee.search_strategy == 0:
                bee.traveled_distance = bee.traveled_distance + point.get_distance_to(honeycomb_point)
                tree.depth_first_search(tree.root, bee, point)

            elif bee.search_strategy == 1:
                visited = []
                queue = []
                bee.traveled_distance = bee.traveled_distance + point.get_distance_to(honeycomb_point)
                tree.bfs(visited, tree.root, queue, bee, point)

            else:
                bee.traveled_distance = bee.traveled_distance + point.get_distance_to(honeycomb_point)
                previous_position = point
                for i in range(len(flowers_in_area)):
                    index = random.randint(0, len(flowers_in_area) - 1)
                    if flowers_in_area[index] == bee.fav_color or random.uniform(0.0, 1.0) <= visiting_a_node_chace:
                        bee.pollinate(flowers_in_area[index])
                        bee.traveled_distance = bee.traveled_distance + previous_position.get_distance_to(
                            Point(flowers_in_area[index].x, flowers_in_area[index].y))
                        previous_position = Point(flowers_in_area[index].x, flowers_in_area[index].y)
        b.append(bee)
    return b

