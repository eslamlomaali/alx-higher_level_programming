#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const y = process.argv.slice(2).map(Number);
  const z = y.sort(function (a, b) { return b - a; })[1];
  console.log(z);
}
