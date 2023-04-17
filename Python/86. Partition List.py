# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        small = ListNode(-1)
        large = ListNode(-1)
        small_head = small
        large_head = large
        while head:
            if head.val < x:
                small.next = head
                head = head.next
                small = small.next
                small.next = None
            else:
                large.next = head
                head = head.next
                large = large.next
                large.next = None
        small.next = large_head.next
        return small_head.next