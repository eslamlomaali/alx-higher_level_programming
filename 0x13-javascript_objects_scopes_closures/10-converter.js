#!/usr/bin/node

exports.converter = function (base) {
  return function (nn) {
    return n.toString(base);
  };
};
