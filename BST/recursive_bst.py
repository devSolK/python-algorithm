class BST:
    # node -------------------
    class Node:
        # Node's init function
        def __init__(self,data=None,left=None,right=None):
              self.data = data
              self.left = left
              self.right = right
    # ------------------------
    #BST's init function
    def __init__(self):
        self.root = None
        
    def insert_helper(self, data, subtree):
        if(subtree==None):
            #nothing inside
            return BST.Node(data)
        elif(data < subtree.data):
            #if data is smaller then sub root
            subtree.left = self.insert_helper(data, subtree.left)
            return subtree
        else:
            subtree.right = self.insert_helper(data, subtree.right)
            return subtree

    def recursive_insert(self, data):
        self.root = self.insert_helper(data, self.root)
        
    def print_inorder(self, subtree):
        if (subtree !=None):
            #if it is not empty
            # left subtree → node → right subtree
            self.print_inorder(subtree.left) # left subtree
            print(subtree.data, end=" ")      # node
            self.print_inorder(subtree.right) # right subtree
        
    def print_preorder(self, subtree):
        if (subtree !=None):
            #if it is not empty
            # node → left subtree →  right subtree
            print(subtree.data, end=" ")       # node
            self.print_preorder(subtree.left) # left subtree
            self.print_preorder(subtree.right) # right subtree

    def print(self):
        self.print_inorder(self.root)
        self.print_preorder(self.root)
        print("")
