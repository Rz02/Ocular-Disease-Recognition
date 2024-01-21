from flask import Flask, render_template, request, redirect, url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the CNN model
model = load_model('models/model6.h5')

# Class labels for prediction
class_labels = ['Normal', 'Diabetes', 'Glaucoma', 'Cataract', 'Age-related Macular Degeneration', 'Hypertension', 'Pathological Myopia', 'Other diseases/abnormalities']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return redirect(request.url)

    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Make a prediction using the model
    prediction = predict_myopia(file_path)

    # Redirect to the homepage with the prediction result
    return render_template('index.html', prediction=prediction)

def predict_myopia(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Make predictions
    predictions = model.predict(img_array)

    # Get the predicted label
    predicted_label = class_labels[np.argmax(predictions)]

    return predicted_label

if __name__ == '__main__':
    app.run(debug=True)
