// 1. letters only: 
// /[a-zA-Z]/

// 2. letters, numbers, spaces, dashes
// a)  /^[\w\d\s-]+$/ 
// b)  /^[0-9A-Za-z\s\-]+$/

// ^ from beginning
// \w letters
// \d digits
// \s space
// and then the - (dash)
// ^wrapping in [ ] matches any character within
// $ to the end