// Given a string s, reverse only all the vowels in the string and return it.

// The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

// Example 1:

// Input: s = "hello"
// Output: "holle"
// Example 2:

// Input: s = "leetcode"
// Output: "leotcede"
 

var reverseVowels = function(s) {
    if (s.length <= 1) { return s; }
    const str = [...s];
    let left = 0;
    let right = s.length - 1;
    const set = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
    
    while(left < right) {
      if (set.has(str[left]) && set.has(str[right])) {
        [str[right], str[left]] = [str[left], str[right]];      
        left++;
        right--;
      } else if (set.has(str[left])) {
        right--;
      } else {
        left++;
      }
    }
    return str.join('');
  };