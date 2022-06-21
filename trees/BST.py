class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root

        while True:
            if new_val > current.value and current.right != None:
                current = current.right
            elif new_val < current.value and current.left != None:
                current = current.left
            else:
                break
        if new_val > current.value:
            current.right = Node(new_val)
        else:
            current.left = Node(new_val)

    def search(self, find_val):
        current = self.root
        
        while True:
            if current.value == find_val:
                return True
            else:
                if find_val > current.value and current.right != None:
                    current = current.right
                elif find_val < current.value and current.left != None:
                    current = current.left
                else:
                    return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
