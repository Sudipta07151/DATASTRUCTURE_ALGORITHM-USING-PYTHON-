from math import floor


class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        c_index = len(self.values) - 1
        while c_index > 0:
            p_index = floor((c_index-1)/2)
            parent = self.values[p_index]
            if value <= parent:
                break
            self.values[p_index] = value
            self.values[c_index] = parent
            c_index = p_index

    def extract_maximum(self):
        if len(self.values) == 0:
            return None
        elif len(self.values) == 1:
            temp=self.values[0]
            self.values.clear()
            return temp
        else:
            index=len(self.values)-1
            value=self.values[0]
            self.values[0]=self.values[index]
            self.values.pop()
            index=0
            while True:
                leftI = (index*2)+1
                rightI = (index*2)+2
                temp=None
                if(leftI < len(self.values)):
                    if self.values[index]<self.values[leftI]:
                        temp=self.values[index]
                        self.values[index]=self.values[leftI]
                        self.values[leftI]=temp
                        index=leftI
                if (rightI < len(self.values)):
                    temp = self.values[index]
                    self.values[index] = self.values[rightI]
                    self.values[rightI] = temp
                    index=rightI
                if temp is None:
                    break
            return value

    def get_heap(self):
        return self.values

