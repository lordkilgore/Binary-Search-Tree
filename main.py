from random import randint

class Node:
    left = None
    right = None
    parent = None

    def __init__(self, key):
        self.key = key

class BinarySearchTree:
    nodeMap = {}

    def __init__(self):
        self.root = Node(None)
    
    def insert(self, key):
        if self.root.key == None:
            self.root.key = key
            self.nodeMap[0] = [key]
        else:
            current = self.root
            level = 1
            while current != None:
                if key < current.key:
                    if current.left == None:
                        current.left = Node(key)
                        current.left.parent = current
                        current = None
                    else:
                        current = current.left
                        level += 1
                else:
                    if current.right == None:
                        current.right = Node(key)
                        current.right.parent = current
                        current = None
                    else:
                        current = current.right
                        level += 1
                
                if current == None:
                    try:
                        self.nodeMap[level].append(key)
                    except KeyError:
                        self.nodeMap[level] = []
                        self.nodeMap[level].append(key)
                
    
    def search(self, key, subtree = "root"):
        if subtree == "root":
            subtree = self.root
    
        if subtree.key == None:
            print(f"Subtree empty.")
            return None
        else:
            current = subtree
            while (current != None):
                if (key == current.key):
                    return current
                elif (key < current.key):
                    current = current.left
                else:
                    current = current.right

            print(f"Key {key} not found in subtree.")
            return None
    
    def getSubtree(self, key):
        return self.search(key)
    
    def remove(self, key, subTree = "root"):
        if self.root.key == None:
            print("Tree is empty.")
        else:
            current = self.search(key, subTree)
            if current != None:
                parent = current.parent
                # Case 1: Removing Leaf Node
                if current.left == None and current.right == None:
                    if current == self.root:
                        self.root.key = None
                        self.nodeMap[0] = [None]
                    else:
                        if parent.left == current:
                            parent.left = None
                        else:
                            parent.right = None
                
                # Case 2: Removing Internal Node w/ 1 Child
                elif current.left != None and current.right == None:
                    if current == self.root:
                        self.root = self.root.left 
                    else:
                        if parent.left == current:
                            parent.left = current.left
                        else:
                            parent.right = current.left
                
                elif current.left == None and current.right != None:
                    if current == self.root:
                        self.root = self.root.right
                    else:
                        if parent.left == current:
                            parent.left = current.right
                        else:
                            parent.right = current.right
                
                # Case 3: Removing Internal Node w/ 2 Children
                else:
                    successor = current.right
                    while successor.left != None:
                        successor = successor.left
                    
                    current.key = successor.key
                    self.remove(successor.key, successor.parent) # O(1) :)
                        
            print(f"Key {key} not found.")

    def printTree(self, subTree = "root", spacing = 50):
        if subTree == "root":
            current = self.root
        else:
            current = subTree
        
        
    def getHeight(self, subTree = "root"):
        if subTree == "root":
            current = self.root
        else:
            current = subTree

        if current == None:
            return -1
        
        leftHeight = self.getHeight(current.left)
        rightHeight = self.getHeight(current.right)

        return 1 + max(leftHeight, rightHeight)


BST = BinarySearchTree()

for i in range(10):
    BST.insert(randint(0, 50))

print(BST.getHeight())
print(BST.nodeMap)

# Make sure that remove() also removes from the NodeMap

# Implement printTree function

        

