fetch('/api/modules/')
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
