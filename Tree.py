from flower_genetic import *
from queue import LifoQueue
from Area import *
from bee_genetic import *
class Node:
    def __init__(self,flower,id,level = 0,right_node = None,center_node = None,left_node = None,visited = False):
        self.flower=flower
        self._id=id
        self.right_node = right_node
        self.center_node = center_node
        self.left_node = left_node
        self._level=level


    def get_quantity_children(self):
        if self.right_node != None:
            return 3
        if self.center_node != None:
            return 2
        if self.left_node != None:
            return 1
        return 0


    def __str__(self):
        return "Node ",self._id," level ",self._level,self.flower.__str__()


class Tree:
    def __init__(self, probability_of_visiting_a_node, nodes = 1 ):
        self.root = None
        self.nodes = nodes
        self.probability_of_visiting_a_node = probability_of_visiting_a_node
    

    def get_height(self, root):
        if root == None:
            return 0
        else:
            return 1 + self.get_height(root.left_node)


    def _get_left_leaf(self, root):
        if(root.left_node == None):
            return root
        else:
            return self._get_left_leaf(root.left_node)
        

    def _look_for_field(self,root,tree_level):
        if (root._level == tree_level - 1 or root._level == tree_level):
            if (root.left_node == None or root.center_node == None or root.right_node == None):
                return root
            
            else:
                return None
            
        elif(self._look_for_field(root.left_node,tree_level) != None):
            return self._look_for_field(root.left_node,tree_level)
        
        elif(self._look_for_field(root.center_node,tree_level) != None):
            return self._look_for_field(root.center_node,tree_level)
        
        elif(self._look_for_field(root.right_node,tree_level) != None):
            return self._look_for_field(root.right_node,tree_level)
        
        return None


    def insert(self, root, flower):
        if(self.root != None):
            field = self._look_for_field(root,self.get_height(root))
            if(field == None):
                field = self._get_left_leaf(root)
            
            self.nodes=self.nodes + 1
            if(field.left_node == None):
                field.left_node =  Node(flower,self.nodes,field._level+1)
            
            elif(field.center_node == None):
                field.center_node =  Node(flower,self.nodes,field._level+1)
            
            elif(field.right_node == None):
                field.right_node =  Node(flower,self.nodes,field._level+1)
            
        else:
            self.root = Node(flower,self.nodes,self.get_height(root)+1)

    def depth_first_search(self,root,bee,previous_position):
        if (root == None):
            return 
        if bee.fav_color == root.flower.color or random.uniform(0.0, 1.0) <= self.probability_of_visiting_a_node:
            
            bee.pollinate(root.flower)
            bee.traveled_distance=bee.traveled_distance + previous_position.get_distance_to(Point(root.flower.x,root.flower.y))
            

        self.depth_first_search(root.left_node,bee,Point(root.flower.x,root.flower.y)); 
        self.depth_first_search(root.center_node,bee,Point(root.flower.x,root.flower.y)); 
        self.depth_first_search(root.right_node,bee,Point(root.flower.x,root.flower.y)); 


    def bfs(self,visited, root, queue,bee,previous_position):
        visited.append(root)
        queue.append(root)
        last=None
        while queue:
            node = queue.pop(0) 
            if node != None:
                if node.flower.color == bee.fav_color or random.uniform(0.0, 1.0) <= self.probability_of_visiting_a_node:
                    bee.pollinate(node.flower)
                    bee.traveled_distance=bee.traveled_distance + previous_position.get_distance_to(Point(node.flower.x,node.flower.y))
                    previous_position = Point(node.flower.x,node.flower.y)
                    last=node.flower

                if node.left_node not in visited:
                    visited.append(node.left_node)
                    queue.append(node.left_node)

                if node.center_node not in visited:
                    visited.append(node.center_node)
                    queue.append(node.center_node)

                if node.right_node not in visited:
                    visited.append(node.right_node)
                    queue.append(node.right_node)
        return last
        
    
    def printPreorder(self,root):
        """just for fun"""
        if (root == None):
            return
        print(root.__str__()) 
        self.printPreorder(root.left_node)  
        self.printPreorder(root.center_node) 
        self.printPreorder(root.right_node)
    
        




        
