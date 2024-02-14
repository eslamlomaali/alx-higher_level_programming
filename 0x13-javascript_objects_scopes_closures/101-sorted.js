#!/usr/bin/node
const d = require('./101-data').d;

const t = Object.entries(d);
const va = Object.values(d);
const vals = [...new Set(va)];
const newd = {};
for (const x in vals) {
  const li = [];
  for (const m in tota) {
    if (tota[m][1] === vals[x]) {
      li.unshift(tota[m][0]);
    }
  }
  newd[vals[m]] = li;
}
console.log(newd);
