function simulate() {
    fetch('/simulate')
        .then(res => res.json())
        .then(data => {
            document.getElementById('output').textContent = JSON.stringify(data, null, 2);
        })
        .catch(err => {
            document.getElementById('output').textContent = 'Error: ' + err;
        });
}