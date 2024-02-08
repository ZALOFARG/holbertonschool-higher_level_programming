const listener = document.getElementById('add_item');
listener.addEventListener('click', () => {
    const new_element = document.createElement('li');
    new_element.textContent = 'Item';

    const father = document.querySelector('.my_list');
    father.appendChild(new_element);
});