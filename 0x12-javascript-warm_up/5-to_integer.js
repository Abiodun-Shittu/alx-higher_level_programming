#!/usr/bin/node
const firstArg = process.argv[2];
if (!firstArg || isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + parseInt(firstArg));
}
