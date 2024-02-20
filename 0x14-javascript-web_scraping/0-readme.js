#!/usr/bin/env node

const fs = require("fs");

if (process.argv.length < 3) {
  console.error("Please provide a file path");
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, "utf-8", (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
