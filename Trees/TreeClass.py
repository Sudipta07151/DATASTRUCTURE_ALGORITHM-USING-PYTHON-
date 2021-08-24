from Node import *

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
       new_node=Node(value)
       if self.root is None:
           self.root=new_node
       temp=self.root
       while True:
           if new_node.value ==temp.value:
               return False
           elif new_node.value<temp.value:
               if temp.left is None:
                   temp.left=new_node
                   return True
               temp=temp.left
           else:
               if temp.right is None:
                   temp.right = new_node
                   return True
               temp = temp.right

    def contains_value(self,value):
        if self.root is None:
            return False
        temp=self.root
        while temp is not None:
            if temp.value == value:
                return True
            elif temp.value<value:
                temp=temp.right
            else:
                 temp=temp.left
        return False