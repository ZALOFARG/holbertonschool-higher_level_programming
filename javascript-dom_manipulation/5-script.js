const selector = document.getElementById('update_header');
selector.addEventListener('click', () => {
    const changedItem = document.querySelector('header');
    changedItem.textContent = 'New Header!!!'
});