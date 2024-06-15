from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
import numpy as np

app = Flask(__name__)
model = load_model('D:/Kuliah/MSIB/Hactiv8id/Capstone/PROJECT/deployment_capstone/densenet_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    file = request.files['image']
    img_bytes = file.read()  # Baca bytes dari file yang diunggah
    img = image.load_img(BytesIO(img_bytes), target_size=(224, 224))  # Ubah bytes menjadi objek BytesIO
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)
    
    # In a real application, you might have a mapping from class indices to class names
    class_names = {0: 'battery', 1: 'glass', 2: 'metal', 3: 'organic', 4: 'paper', 5: 'plastic'}  # Adjust as needed
    
    return jsonify({'prediction': class_names[predicted_class[0]]})

if __name__ == '__main__':
    app.run(debug=True)
