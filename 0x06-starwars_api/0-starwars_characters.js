#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const ApiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request.get(ApiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }
  const characters = body.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  const characterPromises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, { json: true }, (err, res, charBody) => {
        if (err) {
          reject(new Error('Error fetching character:', err));
        } else if (res.statusCode !== 200) {
          reject(new Error(`Failed to fetch character data. Status code: ${res.statusCode}`));
        } else {
          resolve(charBody.name);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => console.log(error));
});
