#!/usr/bin/node
/*
A class square inheriting from Previous rectangle
*/

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
