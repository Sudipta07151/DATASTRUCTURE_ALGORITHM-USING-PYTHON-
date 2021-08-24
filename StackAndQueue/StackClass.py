from Item import *

class Stack:
    def __init__(self,value):
        new_item=Item(value)
        self.top=new_item
        self.height=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push_to_stack(self,value):
        new_item=Item(value)
        new_item.next=self.top
        self.top=new_item
        self.height+=1

    def pop_from_stack(self):
        if self.top is None:
            return None
        elif self.top.next is None:
            temp=self.top
            self.top=None
            self.height-=1
            return temp
        else:
            temp=self.top
            self.top=self.top.next
            self.height -= 1
            return temp



