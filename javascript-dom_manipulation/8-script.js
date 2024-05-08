document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const hello = document.querySelector('#hello');

  fetch(url)
    .then(response => response.json())
    .then(data => {
      hello.textContent = data.hello;
    });
});
