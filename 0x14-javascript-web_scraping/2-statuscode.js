#!/usr/bin/node
const request = require('request');
request(process.argv[2], 'utf-8', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response && response.statusCode);
});
