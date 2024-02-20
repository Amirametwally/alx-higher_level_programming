#!/usr/bin/node
const r = require("request");
const u = "http://swapi.co/api/films/" + process.argv[2];
r(u, (error, response, body) => {
  if (error) console.log(error);
  console.log(JSON.parse(body).title);
});
