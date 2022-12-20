#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  console.log(arr.sort((a, b) => a - b)[arr.length - 2]);
}
