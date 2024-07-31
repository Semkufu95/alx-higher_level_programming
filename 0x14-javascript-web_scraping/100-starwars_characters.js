#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  for (const c of body.characters) {
    request(c, { json: true }, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(body.name);
    });
  }
});
