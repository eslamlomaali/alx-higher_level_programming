#!/usr/bin/node
const loma = require('fs');

const folom = loma.readFileSync(process.argv[2]).toString();
const solom = loma.readFileSync(process.argv[3]).toString();
loma.writeFileSync(process.argv[4], folom + solom);
