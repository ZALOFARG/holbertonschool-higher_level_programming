fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('character').textContent = data.name;
    })