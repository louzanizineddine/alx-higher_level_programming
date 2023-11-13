#!/usr/bin/node
const { argv } = require('process');
const x = Number(argv[2]);
const y = Number(argv[3]);
const add = (x, y) => x + y;
console.log(add(x, y));
