#!/usr/bin/node

exports.converter = function (base) {
  return function (nn) {
    return nn.toString(base);
  };
};
