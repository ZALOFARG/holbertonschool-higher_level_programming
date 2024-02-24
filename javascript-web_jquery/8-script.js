$(document).ready(() => {
  const selector = $('UL#list_movies');

  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    data.results.forEach((movie) => {
      selector.append(`<li>${movie.title}</li>`);
    });
  });
});