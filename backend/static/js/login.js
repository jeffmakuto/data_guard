const loginForm = document.getElementById('login-form');
const errorMessage = document.getElementById('error-message');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // Send AJAX request to login endpoint
    fetch('/api/users/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Invalid username or password');
        }
        return response.json();
    })
    .then(data => {
        // Save token to localStorage or sessionStorage
        sessionStorage.setItem('token', data.access);
        // Redirect to the desired page
        window.location.href = '/dashboard.html'; // Change to the desired page
    })
    .catch(error => {
        errorMessage.textContent = error.message;
    });
});
