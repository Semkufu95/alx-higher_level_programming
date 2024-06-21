#!/usr/bin/node

const args = process.argv;

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
