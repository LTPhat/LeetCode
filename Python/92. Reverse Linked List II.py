# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        values = []   # to stores the values that needed to be reverse
        nodes = []    # to keep track of the nodes which needs to be reverse
        counter = 0
        curr = head
        while curr:
            counter += 1
            if counter >= left and counter <= right:
                values.append(curr.val)     #  | adding value and nodes in the list
                nodes.append(curr)          #  |
            curr = curr.next
        for node in nodes:
            node.val = values.pop(-1)       #  replace the value of nodes
        return head