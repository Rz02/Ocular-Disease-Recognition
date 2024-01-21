document.getElementById('file').addEventListener('change', function (event) {
    const preview = document.getElementById('image-preview');
    const progress = document.getElementById('upload-progress');
    const predictionContainer = document.getElementById('prediction-container');

    if (event.target.files.length > 0) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.classList.remove('hidden');
            progress.classList.remove('hidden');
            predictionContainer.classList.add('hidden');
        };

        reader.readAsDataURL(file);
    }
});

document.getElementById('upload-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting

    const progress = document.getElementById('upload-progress');
    const predictionContainer = document.getElementById('prediction-container');
    const predictionText = document.getElementById('prediction-text');
    const preview = document.getElementById('image-preview');

    // Check if an image is previewed
    if (!preview.classList.contains('hidden')) {
        // Simulate progress bar (you can replace this with real upload logic)
        let value = 0;
        const interval = setInterval(function () {
            value += 10;
            progress.value = value;

            if (value === 100) {
                clearInterval(interval);
                progress.classList.add('hidden');
                predictionContainer.classList.remove('hidden');
                // Replace the following line with your actual prediction logic
                predictionText.innerText = 'Normal'; // Sample prediction result
            }
        }, 500);
    } else {
        alert('Please choose an image before predicting.');
    }
});