#!/usr/bin/node
exports.esrever = function (list) {
  let strng = '';
  for (let k = 0; k < list.length / 2; k++) {
    strng = list[k];
    list[k] = list[list.length - k - 1];
    list[list.length - k - 1] = strng;
  }
  return list;
};
