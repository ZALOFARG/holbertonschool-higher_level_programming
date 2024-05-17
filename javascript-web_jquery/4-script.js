$('document').ready(() => {
  if ($('header').attr('class') === undefined) {
    $('header').addClass('red');
  }

  $('DIV#toggle_header').click(() => {
    $('header').toggleClass('red green');
  })
})
