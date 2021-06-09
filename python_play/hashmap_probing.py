class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash_key(self,key):
        hash_key = 0
        for char in key:
            hash_key+=ord(char)
        return hash_key%self.MAX
    
    def __setitem__(self,key,value):        
        hash_key = self.get_hash_key(key)  
        check_collision = True  
        while check_collision:
            if self.arr[hash_key]:                
                hash_key+=1
                if (hash_key >= self.MAX):
                    hash_key = hash_key%self.MAX
                    continue                                    
            check_collision = False                                      
        self.arr[hash_key] = value    
        
    
    def __getitem__(self,key):
        hash_key = self.get_hash_key(key)        
        if self.arr[hash_key]:
            return self.arr[hash_key]
        return None

ht = HashTable()
ht['march 6'] = 100
ht['march 17'] = 200

print(ht['march 6'])




        

        


