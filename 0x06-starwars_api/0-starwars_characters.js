#!/usr/bin/node
// script that prints all characters of a star wars movie

const request = require('request');

function movieCharacters (url, movieId) {
  const fullUrl = url + movieId.toString();
  let characters = [];
  request(fullUrl, function (error, results) {
    if (error) {
      console.log(error);
    }
    const data = JSON.parse(results.body);
    characters = data.characters;
    // if characters are present. using thir url get their name
    if (characters.length > 0) {
      for (let i = 0; i < characters.length; i++) {
        // get data of each character and extact their name
        request(characters[i], function (error, response) {
          if (error) {
            console.log(error);
          }
          const personObj = JSON.parse(response.body);
          const name = personObj.name;
          console.log(name);
        });
      }
    }
  });
}

const argv = process.argv;
let value = 0;
if (argv.length === 3) {
  value = parseInt(argv[2]);
  if (value) {
    const url = 'https://swapi-api.alx-tools.com/api/films/';

    // call funtion passs in url and movie_id
    movieCharacters(url, value);
  }
}
