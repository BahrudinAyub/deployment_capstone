function classifyImage() {
    const fileInput = document.getElementById('imageUpload');
    const resultDiv = document.getElementById('result');
    
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('image', file);
    
    fetch('/classify', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = `<p>Predicted class: ${data.prediction}</p>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayImage() {
    const fileInput = document.getElementById('imageUpload');
    const imageContainer = document.getElementById('imageContainer');
    
    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const imgElement = document.createElement('img');
        imgElement.src = e.target.result;
        imgElement.id = 'uploadedImage';
        imageContainer.innerHTML = '';
        imageContainer.appendChild(imgElement);
    }

    reader.readAsDataURL(file);
}
