# Recursion and Binary Search Tree Exercises

Do all exercise below w/o using a single loop but use recursion instead, in Python.

## Basic

1. Write a function print_numbers(n) to print the numbers from 1 to n.
2. Write a function say_hello(names) that takes a list of names and says hello to each name in the list (prints them out using print statement).

## Linked Lists

Given this LLNode definition:

class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

And some setup code to create a linked list, for example:

one = LLNode(1)
two = LLNode(2)
one.next = two
three = LLNode(3)
two.next = three
four = LLNode(4)
three.next = four

1. Write a function ll_lookup(node, target) that returns a LLNode whose data equals target. For example, given the above setup, ll_lookup(one, 3) should return the LLNode associated with 3, while ll_lookup(one, 5) should return None, and ll_lookup(three, 1) should return None.

## Binary Search Trees

Make a copy of bst.py and work with that. In in a BTreeNode class is defined which represents a node in a binary search tree. Two functions have also been defined for you:

* bst_insert(tree_node, new_node) - inserts a new node into the tree will keeping the tree in an order state
* bst_pre_order_traversal(tree_node) - performs a pre-order traversal of the tree to print out all the nodes of the tree

1. Write a bst_lookup(tree_node, target) function that searches for a node within the tree which matches the target. Assume the target is an ordered type and can be compared using < or > (both numbers and strings will work).
2. Write a bst_in_order_traversal(tree_node) function that traverses the tree in the right order, such that if you use the traversal to print the elements the tree, for example, you would print the elements in ascending order.
3. Write a bst_min(tree_node) function that returns the smallest node of the tree (the one all the way to the left).

### Bonus Problems

4. Write a bst_find_gt(tree_node, data) function which returns a list of nodes whose value is greater that data.
5. Write a bst_delete(tree_node, target) function to delete the target node from the tree.
6. Write a bst_n_min(tree_node, n) function that returns the smallest n nodes of the tree.
