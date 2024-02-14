#!/usr/bin/node
exports.esrever = function (list) {
  let hh = list.length - 1;
  let x = 0;
  while ((hh - x) > 0) {
    const a = list[hh];
    list[hh] = list[x];
    list[x] = a;
    x++;
    hh--;
  }
  return list;
};
