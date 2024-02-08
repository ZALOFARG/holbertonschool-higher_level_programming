let selector = document.getElementById('red_header')
selector.addEventListener('click', () => {
    let header = document.querySelector('header');
    header.classList.add('red')
});