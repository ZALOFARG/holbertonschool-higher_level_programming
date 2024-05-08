const header = document.querySelector('header');

const target = document.querySelector('#update_header');

target.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
