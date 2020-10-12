# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def condense_linked_list(node):
    if node is None:
        return None

    curr = node
    while curr is not None:
        prev = curr
        while prev.next is not None:
            if prev.next.value == curr.value:
                prev.next = prev.next.next
            else:
                prev = prev.next
        curr = curr.next

    return node
