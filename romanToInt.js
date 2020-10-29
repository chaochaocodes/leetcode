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
  console.log('convert:', number)

  // I can be placed before V (5) and X (10) to make 4 and 9. 
  // X can be placed before L (50) and C (100) to make 40 and 90. 
  // C can be placed before D (500) and M (1000) to make 400 and 900.
  const finalSum = []
  for (i=0; i < number.length; i++) {
    if (number[i]== 100 && (number[i+1]==500 || number[i+1]==1000 )) {
      finalSum.push(number[i+1] - number[i])
      ++i;
    } else if (number[i]== 10 && (number[i+1]==50 || number[i+1]==100 )) {
      finalSum.push(number[i+1] - number[i])
      ++i;
    } else if (number[i]== 1 && (number[i+1]==5 || number[i+1]==10 )) {
      finalSum.push(number[i+1] - number[i])
      ++i;
    } else {
      finalSum.push(number[i])
    }
  } 
  console.log(finalSum)
  return finalSum.reduce(function(a,b) { return a+b}, 0)

};

romanToInt(input5)