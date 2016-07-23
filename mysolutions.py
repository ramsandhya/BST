
## Basic

1. Write a function print_numbers(n) to print the numbers from 1 to n.

def print_numbers (n, m):
    print m
    if n > 1:
        print_numbers(n-1, m+1)

print_numbers(10, 1)

Fancy way:

def print_numbers (n, m + 1):
    print m
    if n > 1:
        print_numbers(n-1, m+1)

print_numbers(10)


2. Write a function say_hello(names) that takes a list of names and says hello to each name in the list (prints them out using print statement).


def say_hello(names, i = 0):

    if i < len(names):
       print "Hello %r" % names[i]
       say_hello(names, i + 1)

say_hello([Bob, Mary], names[i])

def print_items(lst, i = 0):
    if i < len(lst):
        print "print_items %r" % lst[i]
        print_items(lst, i + 1)

print_items([1, 2, 3], lst[i])


## Linked Lists
Extra:
Printing the data in the nodes:

class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

one = LLNode(1)
two = LLNode(2)
three = LLNode(3)
four = LLNode(4)
five = LLNode(5)
six = LLNode(6)
seven = LLnode(7)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven

def ll_print_items(llnode):
    if llnode:
        print "The current node data is %r" % llnode.data
        ll_print_items(llnode.next)

ll_print_items(one)


1. 1. Write a function ll_lookup(node, target) that returns a LLNode whose data equals target. For example, given the above setup, ll_lookup(one, 3) should return the LLNode associated with 3, while ll_lookup(one, 5) should return None, and ll_lookup(three, 1) should return None.


class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return LLNode(%r) % self.data

one = LLNode(1)
two = LLNode(2)
one.next = two
three = LLNode(3)
two.next = three
four = LLNode(4)
three.next = four


def ll_check_items(llnode):
    if llnode:
        print "The current node data is %r" % llnode.data
        ll_check_items(llnode.next)

ll_check_items(one)

# def ll_lookup(llnode, target):
#     ll_check_items(llnode):
#         if node_value == target:
#             print "The current node is %r" % llnode
#             return llnode
#         elif node_value > target:
#             print "The current node is not available %r" % llnode
#             return None
#         elif llnode == 3 && target == 1:
#             return None
#             ll_lookup(llnode + 1, target)
#
# ll_lookup(1, 3)
# ll_lookup(1, 5)
# ll_lookup(3, 1)



def ll_lookup(llnode, target):
    if node:
        if node.data == target:
             return node
        else
            return ll_lookup(node.next, target)

print ll_lookup(one, 3)
print ll_lookup(one, 5)
print ll_lookup(three, 1)

def bst_pre_order_traverse(node, fn, level=0):
    if node is None:
        return
    # center
    fn(node, level)
    # left
    bst_pre_order_traverse(node.left, fn, level + 1)
    # right
    bst_pre_order_traverse(node.right, fn, level + 1)

# Solution
def bst_in_order_traversal(node, fn, level=0):
    if node is None:
        return
    # left
    bst_in_order_traversal(node.left, fn, level + 1)
    # center
    fn(node, level)
    # right
    bst_in_order_traversal(node.right, fn, level + 1)

# Solution for bst_lookup
def bst_lookup(node, target):
    if node:
        if node.data == target:
            return node
        elif target > node.data:
            return bst_lookup(node.right, target)
        else:
            return bst_lookup(node.left, target)

# Solution
def bst_min(node):
    if node:
        if node.left:
            return bst_min(node.left)
        else:
            return node

root_node = BTreeNode(59)
numbers = [57, 13, 65, 6, 44, 29, 21, 82, 96, 95, 71]
for i in numbers:
    bst_insert(root_node, BTreeNode(i))

def printit(node, level):
    print "%r" % node.data

bst_in_order_traversal(root_node, printit)

print bst_lookup(root_node, 100)

print "Min %r" % bst_min(root_node)
