#!/usr/bin/node
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

let firstArg = process.argv[2];
firstArg = parseInt(firstArg);
console.log(factorial(firstArg));
