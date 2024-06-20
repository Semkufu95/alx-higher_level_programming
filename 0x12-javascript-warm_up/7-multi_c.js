#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];

const x = parseInt(firstArg);

if (!isNaN(x)) {
  for (let k = 0; k < x; k++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
