from flask import Flask, render_template, request
import os
import cv2
from service.segmentation import count_plants
from evaluation import evaluate_count  
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')  # This loads your HTML

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file selected"
    file = request.files['image']
    if file.filename == '':
        return "No file selected"
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Read the image and count plants - only once
        image = cv2.imread(filepath)
        plant_count = count_plants(image)

        predicted = plant_count
        actual = 4100 
        false_negatives = max(0, actual - predicted)
        results = evaluate_count(actual, predicted, false_negatives)
        print(results)  # lets you see accuracy in terminal
        
    return render_template(
    'result.html',
    count=plant_count
)
if __name__ == '__main__':
    app.run(debug=True)