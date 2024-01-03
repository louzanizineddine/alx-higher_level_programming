#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const obj = {};
    const todos = JSON.parse(body);

    todos.forEach(todo => {
      if (todo.completed && obj[todo.userId] === undefined) {
        obj[todo.userId] = 1;
      } else if (todo.completed) {
        obj[todo.userId]++;
      }
    });
    console.log(obj);
  }
});
