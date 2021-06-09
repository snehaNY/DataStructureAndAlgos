from BinaryTree import BinaryTree

def balanceTree(ordered):
    bt = BinaryTree()
    addRange(bt,ordered,0,len(ordered))
    return bt

def addRange(bt, ordered,low, high):
    while high >=low:
        mid = (low+high)/2
        bt.add(ordered[mid])
        addRange(bt,ordered,low,mid-1)
        addRange(bt,ordered,mid+1,high)

    


            
