document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok')
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('hello').textContent = data.hello;
        })
})