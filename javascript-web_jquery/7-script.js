$(document).ready(() => {
  const selector = $('DIV#character');

  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    dataType: 'json',
    type: 'GET',
    success: function(data) {
      selector.text(data.name);
    }
  })
})