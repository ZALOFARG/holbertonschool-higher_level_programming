const listOfMovies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const movies = data.results;
        const titles = movies.map(movie => movie.title);

        titles.forEach(title => {
            const item = document.createElement('li');
            item.textContent = title;
            listOfMovies.appendChild(item);
        })
    })