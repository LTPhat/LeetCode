// Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

// Example 1:


// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]
// Example 2:

// Input: head = [5], left = 1, right = 1
// Output: [5]


class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    reverseBetween(head, left, right) {
        let left2right = [];
        let left2rightVal = [];
        let counter = 0;
        let curr = head;
        
        while (curr) {
            counter++;
            if (left <= counter && counter <= right) {
                left2right.push(curr);
                left2rightVal.push(curr.val);
            }
            curr = curr.next;
        }
        
        for (let node of left2right) {
            node.val = left2rightVal.pop();
        }
        
        return head;
    }
}