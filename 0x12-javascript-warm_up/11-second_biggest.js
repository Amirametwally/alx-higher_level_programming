#!/usr/bin/node
let biggestNumber = 0;
const array = [];
let j;

for (j = 2; j < process.argv.length; j++) {
  if (Number.isNaN(parseInt(process.argv[j])) === false) {
    array[j - 2] = parseInt(process.argv[j]);
  }
}

if (array.length > 1) {
  biggestNumber = Math.max.apply(null, array);
  j = array.indexOf(biggestNumber);
  array[j] = 0;
  biggestNumber = Math.max.apply(null, array);
}

console.log(biggestNumber);
