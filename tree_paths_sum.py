# Given the root of a binary tree where each node contains an integer,
# determine the sum of all of the integer values in the tree.
# Example:
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# The expected output given the above tree is
# 5 + 4 + 8 + 11 + 13 + 4 + 7 + 2 + 1, so your function should return 55.
#


# Binary Tree Data Structure
# A tree whose elements have at most 2 children is called a binary tree.
# Since each element in a binary tree can have only 2 children, we typically name them the left and right child.
# A Binary Tree node contains following parts.
#
# Data
# Pointer to left child
# Pointer to right child

# Binary trees are already defined with this interface:
# class Tree(object):
# def __init__(self, x):
# self.value = x
# self.left = None
# self.right = None


def tree_paths_sum(root):

    # if root is not empty return 0
    if root == None:
        return 0
    # take the root  starting value and add it to the root left item and the root right item until
    # we've reached all the values in the tree'
    result = root.value + tree_paths_sum(root.left) + tree_paths_sum(root.right)
    # return the result total
    return result
