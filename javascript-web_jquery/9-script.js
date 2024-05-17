$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data, textStatus) => {
    $('DIV#hello').text(data.hello);
  });
});
