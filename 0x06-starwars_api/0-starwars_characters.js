#!/usr/bin/node
const request = require('request');

function StarWarsAPI (movieID) {
  if (!movieID) {
    console.log('Movie ID is requied');
    return;
  }
  const ApiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

  request(ApiUrl, (error, response, body) => {
    if (error) {
      console.log('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.log(`Failed to fetch data. Status code: ${response.statusCode}`);
      return;
    }
    const movie = JSON.parse(body);
    const characters = movie.characters;

    if (!characters || characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    characters.forEach(characterUrl => {
      request(characterUrl, (err, res, charBody) => {
        if (err) {
          console.log('Error fetching character:', err);
          return;
        }

        if (res.statusCode !== 200) {
          console.log(`Failed to fetch character data. Status code: ${res.statusCode}`);
          return;
        }

        // Parse and display the character name
        const character = JSON.parse(charBody);
        console.log(character.name);
      });
    });
  });
}

const movieID = process.argv[2];
StarWarsAPI(movieID);
