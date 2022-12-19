#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

let firstArg = process.argv[2];
let secondArg = process.argv[3];

firstArg = parseInt(firstArg);
secondArg = parseInt(secondArg);

add(firstArg, secondArg);
