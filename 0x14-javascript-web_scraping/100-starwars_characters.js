#!/usr/bin/node

const r = require('request');
const u = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

r.get(u, (error, response, body) => {
  if (error) console.log(error);
  else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      r.get(character, (error, response, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
