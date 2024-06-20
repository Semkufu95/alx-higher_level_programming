#!/usr/bin/node
const { dict } = require('./101-data');
const occurDict = {};
for (const token in dict) {
  if (occurDict[dict[token]] === undefined) {
    occurDict[dict[token]] = [token];
  } else {
    occurDict[dict[token]] = [...occurDict[dict[token]], token];
  }
}
console.log(occurDict);
