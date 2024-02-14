#!/usr/bin/node
const d = require('./101-data.js').d;

const newd = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (newd[d[occurences]] === undefined) {
    newd[d[occurences]] = [occurences];
  } else {
    newd[d[occurences]].push(occurences);
  }
});
console.log(newd);
