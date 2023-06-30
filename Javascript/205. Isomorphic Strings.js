// Given two strings s and t, determine if they are isomorphic.

// Two strings s and t are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

// Example 1:

// Input: s = "egg", t = "add"
// Output: true
// Example 2:

// Input: s = "foo", t = "bar"
// Output: false
// Example 3:

// Input: s = "paper", t = "title"
// Output: true


/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    function getOrder(s) {
    const map = new Map(), order = [];
    let value = 0;
    for (const char of s) {
      if (!map.has(char)) map.set(char, value++);
      order.push(map.get(char));
    }
    return order;
  }
  return getOrder(s).join() == getOrder(t).join();
    
};