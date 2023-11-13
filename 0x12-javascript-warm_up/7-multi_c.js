#!/usr/bin/node
const { argv } = require('process');
const occ = Number(argv[2]);
const funLoop = () => {
  for (let i = 0; i < occ; i++) {
    console.log('C is fun');
  }
};
isNaN(occ)
  ? (console.log('Missing number of occurrences'))
  : (funLoop());
