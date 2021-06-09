class BinaryTree():
    def __init__(self):
        self.root = None

    def add(self,value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self,target):
        node = self.root
        while node:
            if target is node.value:
                return True
            elif target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
        return False

    def remove(self, value):
        """Remove value from tree"""
        
        if self.root:
            self.root = self.removeFromParent(self.root, value)

    def removeFromParent(self, parent, value):
        """remove value from tree rooted at parent"""
        if parent is None:
            return None
    
        if value == parent.value:
            return parent.delete()
        elif value < parent.value:
            parent.left = self.removeFromParent(parent.left, value)
        else:
            parent.right = self.removeFromParent(parent.right, value)

        return parent

class BinaryNode():    
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self,val):
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)

    def delete(self):
        """
         Remove value of self from BinaryTree. Works in conjunction with remove
         method in BinaryTree
        """

        if self.left == self.right == None:
            return None
        if self.left == None:
            return self.right
        if self.right == None:
            return self.left

        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value

        return self


bt = BinaryTree()
bt.add(10)
bt.add(5)
bt.add(7)
bt.add(3)
bt.add(15)
bt.add(6)
bt.remove(5)



    


    


