#!/usr/bin/node
let firstArg = process.argv[2];
if (!firstArg || isNaN(firstArg)) {
  console.log('Missing size');
} else {
  firstArg = parseInt(firstArg);
  for (let i = 0; i < firstArg; i++) {
    console.log('X'.repeat(firstArg));
  }
}
