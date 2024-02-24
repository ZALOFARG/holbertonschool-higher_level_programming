$(document).ready(() => {
  const selector = $('DIV#hello');

  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    selector.text(data.hello);
  });
});