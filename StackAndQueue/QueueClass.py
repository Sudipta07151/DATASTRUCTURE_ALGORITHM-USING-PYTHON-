from Item import *
class Queue:
    def __init__(self,value):
        new_item=Item(value)
        self.first=new_item
        self.last=new_item
        self.length=1

    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        new_item=Item(value)
        if self.first is None:
            self.first=new_item
            self.last=new_item
        else:
            self.last.next=new_item
            self.last=new_item
        self.length+=1

    def dequeue(self):
        if self.first is None:
            return None
        elif self.first.next is None:
            temp=self.first
            self.first=None
            self.length-=1
            return temp
        else:
            temp=self.first
            self.first=self.first.next
            self.length -= 1
            return temp

