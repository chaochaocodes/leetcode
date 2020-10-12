//https://www.geeksforgeeks.org/program-for-factorial-of-a-number/
//Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.

// ITERATIVE #1 - while, for-loop
findFactorial = (num) => {
	// loop through number
  // num * (num-1) * ... 1
	let arr = [];
  while (num > 0) {
  	arr.push(num)
    num--
  }	

	let result = 1;
	for (i=0; i < arr.length; i++){
  	result *= arr[i]
  }
  return result
}

// ITERATIVE #2
let factorialValueIterative = (num = 0) => {
  let retVal = 1
  for (let i = 1; i < num; i++) {
      retVal += i * retVal
  }
  return retVal
}


// RECURSIVE #1
// Input: Int
// Output: Int

getFactorial = (num) => {
	// base case (where the recursion stops)
  if (num == 1) { return num }
	// for all other cases
  return num * getFactorial(num - 1)
}

console.log("the answer is", getFactorial(5))
//  run: 3 * 2
//  run part a:  2 * 1 = 2
//  run part b:  1


// RECURSIVE #2 
let factorialValueRecursive = (num = 0) => {
  if( num == 0) return 1
  var prevNum = factorialValueRecursive(num - 1)
  return prevNum * num
}