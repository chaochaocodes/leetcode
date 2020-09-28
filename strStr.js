/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
// For the purpose of this problem, return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

// Using match()
var strStr = function(haystack, needle) {
  if (needle.length === 0) return 0;
  let findNeedle = haystack.match(needle)
  return findNeedle === null ? -1 : findNeedle.index
  // match returns null if not found
  // match returns [ 'll', index: 2, input: 'hello', groups: undefined ]
  // or return using indexOf(), https://tc39.es/ecma262/#sec-string.prototype.indexof
  // return needle.length < 1 ? 0 : haystack.indexOf(needle)

};

// Using indexOf which returns -1 when not found
let strStr = (haystack, needle) => haystack.indexOf(needle);
return needle.length < 1 ? 0 : haystack.indexOf(needle)


haystack = "hello", needle = "ll" // 2
haystack = "aaaaa", needle = "bba" // -1
strStr(haystack, needle)
