const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';

const ulTarget = document.getElementById('list_movies');

fetch(URL)
  .then(response => response.json())
  .then(data => {
    const indexes = data.results;
    indexes.forEach(index => {
      const li = document.createElement('li');
      li.textContent = index.title;
      ulTarget.appendChild(li);
    })
  });
