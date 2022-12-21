#!/usr/bin/node
const fs = require('fs');
const firstFile = fs.readFileSync(process.argv[2], 'utf8');
const secondFile = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], firstFile + secondFile);
