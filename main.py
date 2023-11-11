import mergesort

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

                for level, value in enumerate(list(self.nodeMap.values())):
                    if current.key in value:
                        nodeKey = level

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
                    
                    self.nodeMap.get(nodeKey).remove(current.key)
                    return
                
                # Case 2: Removing Internal Node w/ 1 Child
                elif current.left != None and current.right == None:
                    if current == self.root:
                        self.root = self.root.left 
                    else:
                        if parent.left == current:
                            parent.left = current.left
                        else:
                            parent.right = current.left

                    self.nodeMap.get(nodeKey).remove(current.key)
                    self.nodeMap.get(nodeKey).append(current.left.key)
                    self.nodeMap.get(nodeKey + 1).remove(current.left.key)
                    return
                
                elif current.left == None and current.right != None:
                    if current == self.root:
                        self.root = self.root.right
                    else:
                        if parent.left == current:
                            parent.left = current.right
                        else:
                            parent.right = current.right
                    
                    self.nodeMap.get(nodeKey).remove(current.key)
                    self.nodeMap.get(nodeKey).append(current.right.key)
                    self.nodeMap.get(nodeKey + 1).remove(current.right.key)
                    return
                
                # Case 3: Removing Internal Node w/ 2 Children
                else:
                    successor = current.right
                    while successor.left != None:
                        successor = successor.left
                    
                    self.nodeMap.get(nodeKey).remove(current.key)
                    current.key = successor.key
                    self.nodeMap.get(nodeKey).append(current.key)

                    self.remove(successor.key, successor) # O(1) :)   
                    return   
                        
    def getLevel(self, key):
        for level, value in enumerate(list(self.nodeMap.values())):
            if key in value:
                return level

    def printTree(self, subTree = "root", spacing = 50, multiplier = 4):
        # for level, value in enumerate() 
        if subTree == "root":
            subTree = self.root.key
        
        baseLevel = self.getLevel(subTree)
        
        for level in range(len(self.nodeMap) - baseLevel):
            output = ""
            newSpacing = spacing - (multiplier * level)
            output += newSpacing * " "
            mergesort.mergeSort(self.nodeMap.get(level))
            for key in self.nodeMap.get(level):
                node = self.search(key)
                
                if node != self.root and node.parent.left == None:
                    output += ((2 * multiplier - 4) * level) * " "
                
                
                output += ((2 * multiplier - 4) * level) * " "

                output += f"[{key}]"

            print(output)
        
        
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
