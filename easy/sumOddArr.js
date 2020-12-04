var sumOddLengthSubarrays = function(arr) {
  let n, temp, sum;
  n = arr.length;
  sum = 0;
  for(let i=0; i<n;i++){
      temp = arr[i]
      sum += temp
      for(let j = i; j < n-2; j+=2){
          console.log('i,j, temp, sum', i,j,temp,sum)
          temp += arr[j+1] + arr[j+2]
          sum += temp
          console.log('i,j, temp, sum', i,j,temp,sum)
      }
  }
  return sum
};

let input = [1,2,3,4,5]