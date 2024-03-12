# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

# After doing so, return the head of the final linked list.  You may return any such answer.

 

# (Note that in the examples below, all sequences are serializations of ListNode objects.)

# Example 1:

# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
# Example 2:

# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
# Example 3:

# Input: head = [1,2,3,-3,-2]
# Output: [1]
 

# Constraints:

# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mp = {}
        dummy = ListNode(0)
        curr = head
        dummy.next = curr
        mp[0] =  dummy
        prefix_sum = 0

    

        while(curr):
            prefix_sum += curr.val
            # prefix_sum already in mp
            if prefix_sum in mp:
                start = mp[prefix_sum]
                temp = start
                psum = prefix_sum
                while(temp != curr):
                    temp = temp.next
                    psum += temp.val
                    if (temp != curr):
                        del mp[psum]
                # Update remain node
                start.next = curr.next
            else:
                mp[prefix_sum] = curr

            curr = curr.next

        return dummy.next


    