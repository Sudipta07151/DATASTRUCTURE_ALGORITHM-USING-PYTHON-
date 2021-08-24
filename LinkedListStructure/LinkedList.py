from Node import Node

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def get_length(self):
        return self.length

    def append_to_list(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.length+=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1

    def pop_from_list(self):
         if self.head is None:
             return None
         else:
             if self.head.next is None:
                 temp=self.head
                 self.head=None
                 self.tail=None
                 self.length-=1
                 return temp
             else:
                 temp=self.tail
                 ptr=self.head
                 while ptr.next is not None:
                     pre=ptr
                     ptr=ptr.next
                 self.tail=pre
                 self.tail.next=None
                 self.length-=1
                 return temp

    def prepend_to_list(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        else:
            if self.head.next is None:
                temp=self.head
                self.head=None
                self.tail=None
                self.length-=1
                return temp
            else:
                ptr=self.head.next
                temp=self.head
                self.head=ptr
                self.length -= 1
                return temp

    def get_at_index(self,index):
        if self.head is None:
            return None
        elif index>self.length or index<1:
            return None
        else:
            ptr_length=1
            ptr=self.head
            while ptr_length<index:
                ptr=ptr.next
                ptr_length+=1
        return ptr.value

    def set_at_index(self,index,value):
        if index>self.length or index<=0:
            return False
        else:
            ptr=self.head
            for _ in range(1,index):
                ptr=ptr.next
            ptr.value=value
            return True

    def insert_at_index(self,index,value):
        if index > self.length or index <= 0:
            return False
        else:
            if index == 1:
                self.prepend_to_list(value)
                self.length+=1
            elif index == self.length:
                self.append_to_list(value)
                self.length += 1
            else:
                new_node=Node(value)
                ptr=self.head
                pre=None
                for _ in range(1,index):
                    pre=ptr
                    ptr=ptr.next
                new_node.next=pre.next
                pre.next=new_node
                self.length += 1
            return True

    def remove_from_list(self,index):
        if index == 0 or index > self.length:
            return False
        elif index ==1:
            self.pop_first()
            self.length-=1
        elif index==self.length:
            self.pop_from_list()
            self.length -= 1
        else:
           ptr=self.head
           pre=self.head
           for _ in range(1,index):
               pre=ptr
               ptr=ptr.next
           pre.next=ptr.next
           del ptr
           self.length -= 1
        return True
    def reverse_linked_list(self):
        curr=self.head
        self.head=self.tail
        self.tail=curr
        after=curr.next
        before=None
        for _ in range(self.length):
            after=curr.next
            curr.next=before
            before=curr
            curr=after







