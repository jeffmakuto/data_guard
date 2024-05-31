window.onload = () => {
    const token = sessionStorage.getItem('token');
    if (!token) {
        window.location.href = '/login.html'; // Redirect to login page if token is not present
    } else {
        fetchCourses(token);
        fetchModules(token);
        fetchContents(token);
    }
};

function fetchCourses(token) {
    fetch('/api/courses/', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        const coursesList = document.getElementById('courses-list');
        data.forEach(course => {
            const courseElement = document.createElement('div');
            courseElement.classList.add('course');
            courseElement.innerHTML = `
                <strong>Course Title:</strong> ${course.title}<br>
                <strong>Description:</strong> ${course.description || 'N/A'}<br>
                <hr>
            `;
            coursesList.appendChild(courseElement);
        });
    })
    .catch(error => console.error('Error fetching courses:', error));
}

function fetchModules(token) {
    fetch('/api/modules/', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        const modulesList = document.getElementById('modules-list');
        data.forEach(module => {
            const moduleElement = document.createElement('div');
            moduleElement.classList.add('module');
            moduleElement.innerHTML = `
                <strong>Module Title:</strong> ${module.title}<br>
                <strong>Course:</strong> ${module.course.title}<br>
                <strong>Course Description:</strong> ${module.course.description || 'N/A'}<br>
                <strong>Module Description:</strong> ${module.description || 'N/A'}<br>
                <hr>
            `;
            modulesList.appendChild(moduleElement);
        });
    })
    .catch(error => console.error('Error fetching modules:', error));
}

function fetchContents(token) {
    fetch('/api/contents/', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        const contentsList = document.getElementById('contents-list');
        data.forEach(content => {
            const contentElement = document.createElement('div');
            contentElement.classList.add('content');
            contentElement.innerHTML = `
                <strong>Title:</strong> ${content.title}<br>
                <strong>Module:</strong> ${content.module.title}<br>
                <strong>Content Type:</strong> ${content.content_type}<br>
                <a href="${content.file}" download>Download File</a><br>
                <hr>
            `;
            contentsList.appendChild(contentElement);
        });
    })
    .catch(error => console.error('Error fetching contents:', error));
}
