$('document').ready(() => {
  $('DIV#add_item').click(() => {
    let item = "<li>Item</li>";

    $('UL.my_list').append(item);
  });
});
