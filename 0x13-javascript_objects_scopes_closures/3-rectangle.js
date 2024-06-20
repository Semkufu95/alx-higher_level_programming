#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let m = 0; m < this.height; m++) {
      let line = '';
      for (let n = 0; n < this.width; n++) {
        line += 'X';
      }
      console.log(line);
    }
  }
};
