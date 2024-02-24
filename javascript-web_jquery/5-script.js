$(document).ready(() => {
  const list = $('UL.my_list');

  $('DIV#add_item').click(() => {
    const item = '<li>item</li>';
    list.append(item);
  });
});