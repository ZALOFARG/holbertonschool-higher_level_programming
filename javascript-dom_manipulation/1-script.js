const targetHeader = document.querySelector('header');

const targetButton = document.querySelector('#red_header');

targetButton.addEventListener('click', () => {
  targetHeader.style.color = '#FF0000';
});
