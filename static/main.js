// main.js

const form = document.querySelector('form');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  
  const query = event.target.elements.query.value;
  const response = await fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ query })
  });
  
  const data = await response.json();
  const result = data.result;
  const resultElement = document.createElement('p');
  resultElement.textContent = result;
  document.body.appendChild(resultElement);
});
