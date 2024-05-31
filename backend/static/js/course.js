fetch('/api/courses/')
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
