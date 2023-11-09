// You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

// For chosen indices i0, i1, ..., ik - 1, your score is defined as:

// The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
// It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
// Return the maximum possible score.

// A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

 

// Example 1:

// Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
// Output: 12
// Explanation: 
// The four possible subsequence scores are:
// - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
// - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
// - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
// - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
// Therefore, we return the max score, which is 12.
// Example 2:

// Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
// Output: 30
// Explanation: 
// Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.


/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */

class MinHeap {
    constructor(array) {
      this.heap = this.buildHeap(array);
    }
  
    getLength() {
      return this.heap.length;
    }
  
    buildHeap(array) {
      const firstParentIdx = Math.floor((array.length - 2) / 2);
      for (let i = firstParentIdx; i >= 0; i--) {
        this.siftDown(array, i, array.length - 1);
      }
      return array;
    }
  
    peek() {
      return this.heap[0];
    }
  
    siftUp(array) {
      let idx = array.length - 1;
      let parentIdx = Math.floor((idx - 1) / 2);
      while (parentIdx >= 0) {
        if (array[idx] < array[parentIdx]) {
          this.swap(array, idx, parentIdx);
          idx = parentIdx;
          parentIdx = Math.floor((idx - 1) / 2);
        } else {
          break;
        }
      }
    }
  
    insert(num) {
      this.heap.push(num);
      this.siftUp(this.heap);
    }
  
    siftDown(array, idx, endIdx) {
      let leftChildIdx = idx * 2 + 1;
      while (leftChildIdx <= endIdx) {
        let idxToSwap = leftChildIdx;
        let rightChildIdx = idx * 2 + 2;
        if (
          rightChildIdx <= endIdx &&
          array[rightChildIdx] < array[leftChildIdx]
        ) {
          idxToSwap = rightChildIdx;
        }
        if (array[idxToSwap] < array[idx]) {
          this.swap(array, idxToSwap, idx);
          idx = idxToSwap;
          leftChildIdx = idx * 2 + 1;
        } else {
          break;
        }
      }
    }
  
    remove() {
      const valueToRemove = this.heap[0];
      this.swap(this.heap, 0, this.heap.length - 1);
      this.heap.pop();
      this.siftDown(this.heap, 0, this.heap.length - 1);
  
      return valueToRemove;
    }
  
    swap(array, i, j) {
      const temp = array[i];
      array[i] = array[j];
      array[j] = temp;
    }
  }


  
  var maxScore = function (nums1, nums2, k) {
    const array = [];
    const n = nums1.length;
  
    for (let i = 0; i < n; i++) {
      array.push([nums1[i], nums2[i]]);
    }
    array.sort((a, b) => b[1] - a[1]);
  
    let ans = 0;
    let sum = 0;
    const minHeap = new MinHeap([]);
    for (const [valueOne, valueTwo] of array) {
      sum += valueOne;
      minHeap.insert(valueOne);
  
      if (minHeap.getLength() > k) sum -= minHeap.remove();
      if (minHeap.getLength() === k) ans = Math.max(ans, sum * valueTwo);
    }
  
    return ans;
  };
