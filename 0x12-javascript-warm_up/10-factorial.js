#!/usr/bin/node

const firstArg = process.argv[2];
const value = parseInt(firstArg);

function factorial (k) {
  if (isNaN(k)) {
    return 1;
  } else if (k === 0) {
    return 1;
  } else {
    return k * factorial(k - 1);
  }
}

if (!isNaN(value)) {
  console.log(factorial(value));
} else {
  console.log('1');
}
