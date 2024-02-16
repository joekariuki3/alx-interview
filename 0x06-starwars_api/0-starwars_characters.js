#!/usr/bin/node
// script that prints all characters of a star wars movie

const request = require('request');
const { promisify } = require('util');

const asyncRequest = promisify(request);
function movieCharacters (url, movieId) {
  const fullUrl = url + movieId.toString();
  asyncRequest(fullUrl)
    .then(response => {
      const filmData = JSON.parse(response.body);
      const characters = filmData.characters;

      const characterPromises = characters.map(characterUrl => {
        return asyncRequest(characterUrl).then(response => JSON.parse(response.body));
      });

      return Promise.all(characterPromises);
    })
    .then(characters => {
      characters.forEach(character => {
        console.log(character.name);
      });
    })
    .catch(error => {
      console.error('Error:', error);
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
