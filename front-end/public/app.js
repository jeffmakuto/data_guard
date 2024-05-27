document.getElementById('loginForm')?.addEventListener('submit', function(event) {
    event.preventDefault();
    // Handle login logic
    alert('Logged in successfully!');
    window.location.href = 'profile.html';
});

document.getElementById('signupForm')?.addEventListener('submit', function(event) {
    event.preventDefault();
    // Handle signup logic
    alert('Signed up successfully!');
    window.location.href = 'login.html';
});

function logout() {
    // Handle logout logic
    alert('Logged out successfully!');
    window.location.href = 'login.html';
}

function viewCourse(courseId) {
    // Navigate to the selected course page
    window.location.href = courseId + '.html';
}
