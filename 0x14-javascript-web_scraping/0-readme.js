#!/usr/bin/node

let fs = require("fs");

fs.readFile(process.argv[2], 'utf-8', function (err, buf) {
  if (!err) {
    console.log(buf);
  } else {
    console.log(err);
  }
});
