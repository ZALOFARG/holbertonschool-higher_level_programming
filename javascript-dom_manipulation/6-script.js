const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

const target = document.querySelector('#character');

fetch(URL)
  .then(response => response.json())
  .then(data => {
    target.textContent = data.name;
  });
