import queue

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

    # Insert function
    def insert(self, data):
        if self.root is None:
            # if root is none
            # set node's value = data
            self.root = BST.Node(data)
        else :
            #if root is not none
            current = self.root
            inserted = False
            #get current root point(parent)
            #set a flag
            while not inserted:
                if data < current.data:
                    #if data is smaller then root
                    if current.left is not None:
                        #but it is not none
                        current = current.left
                        #set left point as root and let the loop continue
                    else:
                        #if left is not none
                        current.left = BST.Node(data)
                        inserted = True
                        #create node and set value
                        #on the left side of the root
                else:
                #if data is equal or bigger then root
                    if current.right is not None:
                         current = current.right
                    else:
                        current.right = BST.Node(data)
                    inserted = True
                    
    def search(self, data):
        current = self.root
        #get current root **point**(parent)
        while current is not None:
            # if current is none, going back!
            if data < current.data:
                current = current.left
                #if data is smaller then current
                #set left point as root (can be recursive?)
            elif data > current.data:
                #if data is bigger then current
                #search right side!
                current = current.right
            else:
                #data == current.data
                return current
                #found it!
                #return point
        return None
        #if not found.

    def breadth_first_print(self):
        q = queue.Queue()
        #create a queue
        if self.root is not None:
            #if root is not empty
            q.put(self.root)
            #put root in the queue
        while not q.empty():
            #until the queue become empty
            current = q.get()
            #current node is the first node (Dequeue) 
            if current.left:
                q.put(current.left)
                # if left-side child exists,
                #put it into the queue
            if current.right:
                q.put(current.right)
                # right side
            print(current.data, end=" ")
        # continue this until there is no left node
