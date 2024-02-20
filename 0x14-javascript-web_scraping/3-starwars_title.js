#!/usr/bin/node
const r = require('request');
const u = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
r(u, function (error, response, body) {
  console.log(JSON.parse(body).title || error);
});
