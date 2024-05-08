const targetHeader = document.querySelector('header');

const targetToggle = document.getElementById('toggle_header');

targetToggle.addEventListener('click', () => {
  const greenClass = targetHeader.classList.contains('green');
  if (greenClass) {
    targetHeader.classList.replace('green', 'red');
  } else {
    targetHeader.classList.replace('red', 'green');
  }
});
