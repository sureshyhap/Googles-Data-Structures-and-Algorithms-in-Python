class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        present_node = self.root 
        while True:
            if new_val < present_node.value:
                if not present_node.left:
                    present_node.left = Node(new_val)
                    break
                present_node = present_node.left
            else:
                if not present_node.right:
                    present_node.right = Node(new_val)
                    break
                present_node = present_node.right
            

    def search(self, find_val):
        present_node = self.root
        while True:
            if find_val < present_node.value:
                if not present_node.left:
                    return False
                present_node = present_node.left
            elif find_val > present_node.value:
                if not present_node.right:
                    return False
                present_node = present_node.right
            else:
                return True
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
