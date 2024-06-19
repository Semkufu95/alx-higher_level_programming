#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];

const size = parseInt(firstArg);

if (!isNaN(size)) {
  for (let k = 0; k < size; k++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
