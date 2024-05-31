fetch('/api/courses/')
    .then(response => response.json())
    .then(data => {
        const coursesList = document.getElementById('courses-list');
        data.forEach(course => {
            const courseElement = document.createElement('div');
            courseElement.classList.add('course');
            courseElement.textContent = course.title;
            courseElement.textContent = course.description;
            coursesList.appendChild(courseElement);
        });
    })
    .catch(error => console.error('Error fetching courses:', error));
