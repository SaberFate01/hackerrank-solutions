# Tree: Pre order search
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root):
    if root is None:
        return None

    print(root.info, end=" ")
    preOrder(root.left) #Must be complete before reaching next line
    #So it will dive deeper and deeper on left side till none
    preOrder(root.right)
    #After the prev node returns none, it goes right
    #And next cycle it explores the left of the node again


"""
With while loop, post order
"""


def preOrder(root):
    order = [root]
    while len(order) > 0:
        curr = order.pop() #It is a stack! Pop will remove the first element of list!
        if curr is None:
            continue
        print(curr.info, end=' ')
        order += [curr.left, curr.right]  # change right to left for pre order
        # for i in range(len(order)):
        #    print(order[i], end=' ')

# GPT Version


def preOrder(root):
    if root is None:
        return

    # Initialize the stack with the root node
    order = [root] #Stack

    # Continue until the stack is empty
    while order:
        # Pop the current node from the stack
        curr = order.pop() #It is a stack! Pop will remove the first element of list!
        print(curr.info, end=' ')  # Visit the current node

        # Add the right child first (if it exists) so that the left child is processed first
        if curr.right:
            order.append(curr.right)
        # Add the left child to the stack
        if curr.left:
            order.append(curr.left)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)


#No prefix set: bad problem

def noPrefix(words):
    # Write your code here
    encoder = dict()
    for s in words:
        tempdict = encoder
        for i,l in enumerate(s):
            if l in tempdict.keys():
                tempdict = tempdict.get(l)
                if tempdict is True or i==len(s)-1: # cases 1 and 2
                    print(f'BAD SET\n{s}')
                    return
            else: # case 3
                if i==len(s)-1:
                    tempdict[l] = True
                else:
                    tempdict[l] = dict()
                    tempdict = tempdict[l]
    print('GOOD SET')
