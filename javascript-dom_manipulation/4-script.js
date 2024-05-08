const divTarget = document.querySelector('#add_item');

const ulTarget = document.querySelector('ul.my_list');

divTarget.addEventListener('click', () => {
  const liChild = document.createElement('li');
  liChild.textContent = 'Item';
  ulTarget.appendChild(liChild);
});
