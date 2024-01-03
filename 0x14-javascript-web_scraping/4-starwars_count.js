#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    let count = 0;

    movies.forEach(movie => {
      const hasCharacter18 = movie.characters.some(character => character.endsWith('/18/'));
      if (hasCharacter18) {
        count++;
      }
    });

    console.log(count);
  }
});
