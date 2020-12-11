import math
class Point:
    def __init__(self, x, y):
        """
        Sspecified by (x,y) coordinates 
        """
        self.x = x
        self.y = y
    def get_distance_to(self, point):
        """ Returns the distance to another point.
            Args:
                point (:obj:'Point'):  point1.
            Returns:
                float: Distance to the  point1.
        """
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

class Area:
    def __init__(self, points):
        """
        points: a list of Points in clockwise order.
        """
        self.points = points

        
    @property
    def edges(self):
        ''' generates each of the edges with the vertices '''
        edges = []
        for i,p in enumerate(self.points):
            point_1 = p
            point_2 = self.points[(i + 1) % len(self.points)]
            edges.append((point_1,point_2))

        return edges


    def contains(self, point):
            import sys
            _huge = sys.float_info.max
            _eps = 0.00001


            inside = False
            for edge in self.edges:
                A, B = edge[0], edge[1]
                if A.y > B.y:
                    A, B = B, A

                if point.y == A.y or point.y == B.y:
                    point.y += _eps

                if (point.y > B.y or point.y < A.y or point.x > max(A.x, B.x)):
                    continue

                if point.x < min(A.x, B.x): 
                    inside = not inside
                    continue

                try:
                    m_edge = (B.y - A.y) / (B.x - A.x)
                except ZeroDivisionError:
                    m_edge = _huge

                try:
                    m_point = (point.y - A.y) / (point.x - A.x)
                except ZeroDivisionError:
                    m_point = _huge

                if m_point >= m_edge:
                    inside = not inside
                    continue

            return inside
