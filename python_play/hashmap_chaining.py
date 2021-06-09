class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash_key(self,key):
        hash_key = None
        for char in key:
            hash_key+=ord(char)
        return hash_key%self.MAX
    
    def __setitem__(self,key,value):
        hash_key = self.get_hash_key(key)
        if_collision = False
        for idx, elem in enumerate(self.arr[hash_key]):
            if (len(elem) == 2 and elem[0] == key):
                self.arr[hash_key][idx] = (key,value)
                if_collision = True
        if not if_collision:
            self.arr[hash_key].append((key,value))
    
    def __getitem__(self,key):
        hash_key = self.get_hash_key(key)
        for elem in self.arr[hash_key]:
            if elem[0] == key:
                return elem[1]
        return None




        

        


