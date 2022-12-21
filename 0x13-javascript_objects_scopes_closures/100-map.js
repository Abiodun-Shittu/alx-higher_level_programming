#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((item, index) => item * index);

console.log(list);
console.log(newList);
