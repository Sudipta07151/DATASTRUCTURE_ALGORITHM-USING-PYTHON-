class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size

    def hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23)%len(self.data_map)
        return my_hash

    def set_item(self,key,value):
        index=self.hash(key)
        if self.data_map[index] is None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index=self.hash(key)
        if self.data_map[index] is None:
            return None
        for item in self.data_map[index]:
            if item[0]==key:
                return item[1]
        return None

    def get_all_keys(self):
        all_keys=[]
        for at_index in self.data_map:
            if at_index is not None:
                for inside_item in at_index:
                    all_keys.append(inside_item[0])
        return all_keys
    def print_table(self):
        for items in self.data_map:
            print(items)

