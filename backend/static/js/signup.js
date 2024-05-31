const signupForm = document.getElementById('signup-form');
const errorMessage = document.getElementById('error-message');

signupForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = signupForm.username.value;
    const password = signupForm.password.value;

    // Send AJAX request to register endpoint
    fetch('/api/users/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Username already exists');
        }
        return response.json();
    })
    .then(data => {
        // Redirect to login page
        window.location.href = '/login.html';
    })
    .catch(error => {
        errorMessage.textContent = error.message;
    });
});
