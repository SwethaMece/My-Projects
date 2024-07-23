document.getElementById('guidanceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    
    fetch('/submit', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <h2>Guidance for ${data.name}</h2>
            <p>${data.message}</p>
        `;
    })
    .catch(error => console.error('Error:', error));
});

