#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
if (!process.argv[2] || isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + firstArg);
}
