// Given the head of a singly linked list, return true if it is a 
// palindrome
//  or false otherwise.

 

// Example 1:


// Input: head = [1,2,2,1]
// Output: true
// Example 2:


// Input: head = [1,2]
// Output: false

// Straight and Reverse string

//  * Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
 }
 
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let left2right = '';
    let right2left = '';
    while (head){
        left2right += head.val;
        right2left = head.val + right2left;
        head = head.next;
    }
    return left2right === right2left;

};


// C2: Reverse two half and compare

var isPalindrome = function(head){
    let slow = head;
    let fast = head;
    //Find the middle element
    while(fast && fast.next){
        slow = slow.next;
        fast = fast.next.next;
    }
    // Reverse from the middle to the end
    let reversed = null;
    let next = null;
    let cur = slow;
    while(cur){
        next = cur.next;
        cur.next = reversed;
        reversed = cur;
        cur = next;
    }
    // Traverse two half of linked list
    while(head && reversed){
        if (head.val != reversed.val){
            return false;
        }
        reversed = reversed.next;
        head = head.next;
    }
    return true;
}