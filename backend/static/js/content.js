fetch('/api/contents/')
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
