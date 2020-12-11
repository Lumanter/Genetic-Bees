from Area import *
from flower_genetic import *
from Tree import *
from math import cos, sin, radians, degrees
import bisect



def get_coordinates_around_center( angle, distance):
        """ Returns the x,y coordinates around the sonar center from a given angle and distance.

            Args:
                angle (float): Rotation value from the sonar perspective .
                distance (int): Distance from the sonar to the coordinates.

            Returns:
                :obj:`list` of float: Tuple of coordinates.
        """
        center = panal
        point = Point(center.x+distance, center.y) # initial point to rotate
        x = center.x + cos(angle) * (point.x - center.x) - sin(angle) * (point.y - center.y)
        y = center.x + sin(angle) * (point.x - center.x) + cos(angle) * (point.y - center.y)
        return x, y



def get_bee_path_area(direction,deflection,starting_point,distance):
    left_angle = direction - (deflection)
    left_angle = (left_angle + 360) if (left_angle < 0) else left_angle  # adjust over 360 angle
    right_angle = direction + (deflection)
    right_angle = (right_angle - 360) if (right_angle > 360) else right_angle # adjust negative angle
    
    left_point = get_coordinates_around_center(left_angle,distance)
    right_point = get_coordinates_around_center(right_angle,distance)

    area=Area([Point(right_point[0],right_point[1]),Point(left_point[0],left_point[1]),starting_point])
    return area




def get_flowers_in_the_area(area,flowers):
    flowers_in_the_area=[]
    for i in flowers:
        point=Point(i.x,i.y)                            
        #print(i.x,i.y)
        if area.contains(point):
            flowers_in_the_area.append(i)
    return flowers_in_the_area

def set_flower_point_distance(flowers,starting_point):
    print("flowers in the area",flowers)
    flows=[]
    distances=[]
    for flower in flowers:
        point=Point(flower.x,flower.y)
        d=point.get_distance_to(starting_point)
        
        position = bisect.bisect(distances, d)
        bisect.insort(distances, d)
        flows.insert(position,flower)
    for flower in flows:
        point=Point(flower.x,flower.y)
        d=point.get_distance_to(starting_point)
        print("distancia: ",d)
    return flows

if __name__ == "__main__":
    
    
    panal = Point(64,64)
    distance = 20
    desviacion = 20              
    direccion = 270

    flowers=generate_initial_flowers()
    print("initial flowers:", flowers)
    print("-------")

    flowers_in_area = get_flowers_in_the_area(get_bee_path_area(direccion,desviacion,panal,distance),flowers)
    set_flower_point_distance(flowers_in_area,panal)

    arbol=Tree()
    if flowers_in_area :
        for i in flowers_in_area:
            arbol.insert(arbol.root,i)

        bees = generate_initial_bees()
        visited=[]
        queue=[]
        arbol.depth_first_search(arbol.root,bees[0],Point(arbol.root.flower.x,arbol.root.flower.y))
        arbol.bfs(visited,arbol.root,queue,bees[0],Point(arbol.root.flower.x,arbol.root.flower.y))