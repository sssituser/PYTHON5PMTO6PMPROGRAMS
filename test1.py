# Step 1: Create a Node class
class Node:
    def __init__(self, data):
        self.data = data      # value
        self.left = None      # left child
        self.right = None     # right child


# Step 2: Create nodes
root = Node(10)
root.left = Node(5)
root.right = Node(20)

# Step 3: Print values
print("Root:", root.data)
print("Left Child:", root.left.data)
print("Right Child:", root.right.data)