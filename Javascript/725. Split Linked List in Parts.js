// Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

// The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

// The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

// Return an array of the k parts.

 

// Example 1:


// Input: head = [1,2,3], k = 5
// Output: [[1],[2],[3],[],[]]
// Explanation:
// The first element output[0] has output[0].val = 1, output[0].next = null.
// The last element output[4] is null, but its string representation as a ListNode is [].
// Example 2:


// Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
// Output: [[1,2,3,4],[5,6,7],[8,9,10]]
// Explanation:
// The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 

// Constraints:

// The number of nodes in the list is in the range [0, 1000].
// 0 <= Node.val <= 1000
// 1 <= k <= 50

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode[]}
 */
var splitListToParts = function(head, k) {
    let ans = [];
        let count = 0;
        let curr = head;
        
        // Count number of nodes
        while (curr) {
            count += 1;
            curr = curr.next;
        }
        
        const split_length = Math.floor(count / k);
        let remain = count % k;

        curr = head;
        for (let i = 0; i < k; i++) {
            // Create new node each splited part
            let ptr = new ListNode();
            let sub_head = ptr;
            
            for (let j = 0; j < split_length + (remain > 0 ? 1 : 0); j++) {

                ptr.next = curr;
                curr = curr.next;
                ptr = ptr.next;
            }
            
            if (remain > 0) {
                remain -= 1;
            }

            ptr.next = null;
            ans.push(sub_head.next);
        }
        
        return ans;
};