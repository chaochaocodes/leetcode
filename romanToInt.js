// Symbol   Value
// I        1
// V        5
// X        10
// L        50
// C        100
// D        500
// M        1000

// TEST CASES: 
// input1 = "III"  // 3
// input2 = "IX"   // 9
// input3 = "LVIII"  // 58   L=50 + 5 + 111
// input4 = "MCMXCIV"  // 1994, M=1000, CM= 900, XC= 90, IV= 4
// input5 = "IV" //4

// 1) Using switch, for loop, reduce
var romanToInt = function(s) {
  const number = []
  for (i=0; i<s.length; i++) {
    switch(s[i]) {
      case "I": 
        number.push(1)
        break;
      case "V":
        number.push(5)
        break;
      case "X": 
        number.push(10)
        break;
      case "L":
        number.push(50)
        break;
      case "C":
        number.push(100)
        break;
      case "D": 
        number.push(500)
        break;
      case "M":
        number.push(1000)
        break;
    }
  }

  // I can be placed before V (5) and X (10) to make 4 and 9. 
  // X can be placed before L (50) and C (100) to make 40 and 90. 
  // C can be placed before D (500) and M (1000) to make 400 and 900.
  const result = []
  for (i=0; i < number.length; i++) {
    if (number[i]< number[i+1]) {
      result.push(number[i+1] - number[i])
      ++i;
    } else {
      result.push(number[i])
    }
  } 
  console.log(result)
  return result.reduce(function(a,b) { return a+b }, 0)

};


// 2) Using Map(), while loop
// const romanToInt = s => {
//   if (!s || s.length === 0) {
//     return 0;
//   }

//   const map = new Map([['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]);

//   let i = s.length - 1;
//   let result = map.get(s[i]);

//   while (i > 0) {
//     const curr = map.get(s[i]);
//     const prev = map.get(s[i - 1]); 

//     if (prev >= curr) {
//       result += prev;
//     } else {
//       result -= prev;
//     }

//     i--;
//   }

//   return result;
// };