#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, response, body) => {
  if (err) console.log(err);
  const completeTask = {};
  for (const todo of body) {
    if (todo.completed) {
      completeTask[todo.userId] = (completeTask[todo.userId] || 0) + 1;
    }
  }
  console.log(completeTask);
});
