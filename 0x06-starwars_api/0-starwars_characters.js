#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function sendRequest(characterList) {
  try {
    const requests = characterList.map(characterUrl => axios.get(characterUrl));
    const responses = await Promise.all(requests);

    for (const response of responses) {
      console.log(response.data.name);
    }
  } catch (error) {
    console.log(error);
  }
}

axios.get(movieEndpoint)
  .then(response => {
    const characterList = response.data.characters;
    sendRequest(characterList);
  })
  .catch(error => {
    console.log(error);
  });
