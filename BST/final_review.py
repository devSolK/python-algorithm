from typing import Optional

# NOTE:
#     What if iterative?
#     What if recursive?
#     What if no helper function allowed?
#     Is this BFS? or DFS? (traversal)
#     Time complexity (when balanced / not balanced)

class BST:
    # node -------------------
    class Node:
        # Node's init function
        def __init__(self, value=None, left=None, right=None):
          self.value = value
          self.left = left
          self.right = right
    # ------------------------
    #BST's init function
    def __init__(self):
        self.root: Optional[BST.Node] = None
        
    # =================================== 5
    #This function prints every value in the tree
    #that is between min and max inclusive.
    #Function only visits a subtree where the values may be valid.
        #left side
        #if data > min, left.value < min (x)
        #               right.value (o)
        #right side
        #if data < max, left.value (o)
        #                right.value > max (x)
        #print: min <= data <= max    
    def print_helper(self, subtree, min, max):
        if subtree is not None:
            if subtree.value > min:
                self.print_helper(subtree.left, min, max)
            if min <= subtree.value <= max:
                print(subtree.value, end=" ")
            if subtree.value < max:
                self.print_helper(subtree.right, min, max)

    def print_between_recursive(self, min, max):
        self.print_helper(self.root, min, max)
        print("END")

    def print_between_iterative(self, min, max):
        list = []
        curr = self.root
        while list or curr:
            # left subtree first
            while curr:
                if curr.value > min:
                    list.append(curr)
                    curr = curr.left
                else:
                    # skip left node
                    list.append(curr)
                    curr = None
            node = list.pop()
            if min <= node.value <= max:
                print(node.value, end=" ")
            # right subtree when node.value < max
            if node.value < max:
                curr = node.right
            else:
                curr = None
        print("END")
# =================================== 15
    def inorder_successor(self, value):
        return inorder_successor_helper(self.root, value)

    def inorder_successor_helper(self, subtree, value):
        #...

# =================================== 6
class BT:
    class Node:
        # Node's init function
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    #BT's init function
    def __init__(self):
        self.root = None
        
    #returns the height of the binary tree.
    # def height(self):
    # always forgot putting 'self.' when calling functions...
    def height_helper_recursive(self, subtree):
        if subtree is not None:
            l_height = self.height_helper_recursive(subtree.left)
            r_height = self.height_helper_recursive(subtree.right)
            return 1 + max(l_height, r_height)
        else:
            return 0

    def height(self):
        return self.height_helper_recursive(self.root)



