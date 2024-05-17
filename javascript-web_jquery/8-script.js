$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
    data.results.forEach(elem => {
      $('UL#list_movies').append(`<li>${elem.title}</li>`);
    });
  });
});
