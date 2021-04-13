// create an array of 'false' elements
// if not prime, set array element = true
// compare to number of false's
// optimization: only compare old numbers

var countPrimes = function(n) {
  const arr = new Array(n);
  arr.fill(false);
  let count = 0;
  if (n > 2) count = 1;
  for (let i = 3; i < n; i += 2) {
    if (arr[i] === false) {
      count++;
      for (let j = 3; i * j < n; j += 2) {
        arr[i * j] = true;
      }
    }
  }
  
  return count;
};