class Node():
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RBTree():
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def fixInsert(self, k):
        while k.parent.color == 1:  # While parent is red
            if k.parent == k.parent.parent.right:  # if parent is right child of its parent
                u = k.parent.parent.left  # Left child of grandparent
                if u.color == 1:  # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0  # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1  # Set grandparent node as Red
                    k = k.parent.parent  # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.parent.left:  # If k is left child of it's parent
                        k = k.parent
                        self.RR(k)  # Call for right rotation
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:  # if parent is left child of its parent
                u = k.parent.parent.right  # Right child of grandparent
                if u.color == 1:  # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0  # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1  # set color of grandparent as Red
                    k = k.parent.parent  # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.parent.right:  # if k is right child of its parent
                        k = k.parent
                        self.LR(k)  # Call left rotate on parent of k
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)  # Call right rotate on grandparent
            if k == self.root:  # If k reaches root then break
                break
        self.root.color = 0

    # Insert New Node
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1  # Set root colour as Red

        y = None
        x = self.root

        while x != self.NULL:  # Find position for new node
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y  # Set parent of Node as y
        if y == None:  # If parent i.e, is none then it is root node
            self.root = node
        elif node.val < y.val:  # Check if it is right Node or Left Node by checking the value
            y.left = node
        else:
            y.right = node

        if node.parent == None:  # Root node is always Black
            node.color = 0
            return

        if node.parent.parent == None:  # If parent of node is Root Node
            return
        self.fixInsert(node)

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node
        # Code for left rotate

    def LR(self, x):
        y = x.right  # Y = Right child of x
        x.right = y.left  # Change right child of x to left child of y
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent  # Change parent of y as parent of x
        if x.parent == None:  # If parent of x == None ie. root node
            self.root = y  # Set y as root
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        # Code for right rotate

    def RR(self, x):
        y = x.left  # Y = Left child of x
        x.left = y.right  # Change left child of x to right child of y
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent  # Change parent of y as parent of x
        if x.parent == None:  # If x is root node
            self.root = y  # Set y as root
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, node, key):
        z = self.NULL
        while node != self.NULL:  # Search for the node having that value/ key and store it in 'z'
            if node.val == key:
                z = node

            if node.val <= key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:  # If Kwy is not present then deletion not possible so return
            return 0
        else:
            return 1

        # Function to print

    def __printCall(self, node, indent, last):
        if node != self.NULL:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.val) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    # Function to call print
    def print_tree(self):
        self.__printCall(self.root, "", True)

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def maxDepth(self, node):
        if node is None:
            return -1

        else:

            # Compute the depth of each subtree
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

            # Use the larger one
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1

    def numberofNodes(self, node):
        if node is self.NULL:
            return 0
        else:
            return 1 + self.numberofNodes(node.left) + self.numberofNodes(node.right)


def loadDICT():
    bst = RBTree()
    with open('EN-US-Dictionary.txt') as file:
        for line in file:
            bst.insertNode(line.strip())
        print("successfully loaded")
        return bst


def InsertWord(bst):
    word = str(input("enter the word you wont to insert"))
    if bst.search(bst.root, word) == 0:
        bst.insertNode(word)
    else:
        print("ERROR, word already in the dict")


def menu():
    x = 1
    while x != 0:
        print(
            "1->load dictionary" + "\n" + "2->print dictionary size" + "\n" + "3->insert word" + "\n" + "4->look-up a word" + "\n" + "0->exit")
        x = int(input("enter your choice "))
        if x == 1:
            bst = loadDICT()
            print("max depth = " + str(bst.maxDepth(bst.root)))
        elif x == 2:
            print(bst.numberofNodes(bst.root))
        elif x == 3:
            InsertWord(bst)
            print("max depth = " + str(bst.maxDepth(bst.root)))
            print("max size = " + str(bst.numberofNodes(bst.root)))

        elif x == 4:
            word = input("enter the word you want to search for")
            if bst.search(bst.root, word) == 1:
                print("FOUND")
            else:
                print("NOT FOUND")


if _name_ == "_main_":
    menu()