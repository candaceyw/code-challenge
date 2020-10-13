# Given a linked list of integers, remove any nodes from the linked list
# that have values that have previously occurred in the linked list.
# Your function should return a reference to the head of the updated linked list.
#
# Example:
# Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
# Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
# Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# While the current node is not null
# We want to check if the current node is equal to the next node value.
# Then we'll go to the next node to set that as the current. and travers through each to see if are equal'
# deleting the node by setting the next to the next node by doing this we remove the reference to that duplicate node.
# (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
# So when 3 matches to 3, we skip over that reference and go to the next one.
# Which ultimately will delete that reference to our linked list.

def condense_linked_list(node):
    # if node doesn't exist. Return None
    if node is None:
        return None

    # changing node to current to keep track of what we are comparing
    curr = node
    # so while the current node isn't empty, we'll traverse through the list
    while curr is not None: # O(n) while n is the current node
        # Reference a previous node so we can check with the current
        prev = curr
        # so while the next node isn't empty, we'll traverse through the list
        while prev.next is not None: # O(n) while prev is the current node
            # if the next node equals the current value node
            if prev.next.value == curr.value:
                # we'll remove the reference to that node by skipping over and checking the next
                prev.next = prev.next.next
            else:
                # checking the next node
                prev = prev.next
        curr = curr.next

    # return the final list with duplicate references removed.
    return node

# since we traverse through while we know that current node is not 0,
# the final is O(n) times, with a space complexity of O(n)
