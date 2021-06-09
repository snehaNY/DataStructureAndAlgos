def binary_search(collection,target):
    high = len(collection) - 1
    low = 0
    
    while high >= low:
        mid = (low+high)//2
        if collection[mid] == target:
            return True
        elif collection[mid] > target:
            high  = mid -1
        elif collection[mid] < target:
            low = mid + 1
    return False
    
def linear_search(collection, target):
    return target in collection

def binary_search_insert(collection, target):
    #return the index value that needs to be inserted. 
    low = 0
    high = len(collection) -1
    while high >= low:
        mid = (low+high)//2
        if collection[mid] == target:
            return -1
        elif target > collection[mid]:
            low = mid+1
        else:
            high = mid - 1
    return low

def insert_inplace(ordered, target):
    idx = binary_search_insert(ordered,target)
    ordered.insert(idx,ordered)

def insert_linear(ordered, target):
    for i in ordered:
        if ordered[i]>target:
            ordered.insert(i,target)
       
from time import time
def performance():
    n = 1024
    while n < 50000000:
        sorted = list(range(n))
        now = time()
        insert_linear(sorted,n+1)
        done = time()
        snap = (done-now)*1000
        print("Time taken to insert {0}: {1}".format(n,snap))
        n *=2

if __name__ == "__main__":
    performance()

    
