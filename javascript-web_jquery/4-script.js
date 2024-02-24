const headerElement = $('header');

$(document).ready(function() {
  $('DIV#red_header').on('click',() => {
    const currentClass = headerElement.attr('class');
    
    if(currentClass === 'green') {
      headerElement.toggleClass(`${currentClass} red`);
    } else if (currentClass === 'red') {
      headerElement.toggleClass(`${currentClass} red`);
    }
  });
});