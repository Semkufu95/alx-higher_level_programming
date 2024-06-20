#!/usr/bin/node
const dict = require('./101-data').dict;
const occurDict = {};
for (const token in dict) {
  if (occurDict[dict[token]] === undefined) {
    occurDict[dict[token]] = (token);
  } else {
    occurDict[dict[token]].push(token);
  }
}
console.log(occurDict);
