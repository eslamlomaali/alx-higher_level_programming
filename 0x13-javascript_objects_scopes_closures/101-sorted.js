#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newd = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (newd[dict[occurences]] === undefined) {
    newd[dict[occurences]] = [occurences];
  } else {
    newd[dict[occurences]].push(occurences);
  }
});
console.log(newd);
