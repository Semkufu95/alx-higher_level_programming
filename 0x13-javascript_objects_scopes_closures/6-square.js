#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let m = 0; m < this.width; m++) {
      let line = '';
      for (let k = 0; k < this.height; k++) {
        line += c;
      }
      console.log(line);
    }
  }
};
