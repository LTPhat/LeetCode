// Given the root of a binary tree, return the maximum width of the given tree.

// The maximum width of a tree is the maximum width among all levels.

// The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

// It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

// Example 1:


// Input: root = [1,3,2,5,3,null,9]
// Output: 4
// Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
// Example 2:


// Input: root = [1,3,2,5,null,null,9,6,null,7]
// Output: 7
// Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
// Example 3:


// Input: root = [1,3,2,5]
// Output: 2
// Explanation: The maximum width exists in the second level with length 2 (3,2).


// /**
//  * Definition for a binary tree node.
//  * function TreeNode(val, left, right) {
//  *     this.val = (val===undefined ? 0 : val)
//  *     this.left = (left===undefined ? null : left)
//  *     this.right = (right===undefined ? null : right)
//  * }
//  */
// /**
//  * @param {TreeNode} root
//  * @return {number}
//  */
// */

const widthOfBinaryTree = root => {
	let max = 0;
	const queue = [[root, 0]]; // [node, index]

	if (!root) return 0;

	while (queue.length) {
		const len = queue.length;
		let first = queue[0][1]; // 1st idx
		let last = queue[len - 1][1]; // last idx

		for (let i = 0; i < len; i++) {
			const [node, idx] = queue.shift();
			const subIdx = idx - first; 

			if (node.left) queue.push([node.left, subIdx * 2 + 1]); // find next left idx & node
			if (node.right) queue.push([node.right, subIdx * 2 + 2]); // find next right idx & node
		}

		const width = last - first + 1; // add 1, 0-index based
		max = Math.max(max, width);
	}

	return max;
};
