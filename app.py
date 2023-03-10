import os
import sys
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
import torch
import torch.nn as nn
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import time
from PIL import Image

UPLOAD_FOLDER = 'static/uploads/'
DATA_TRANSFORMS = transforms.Compose([
        transforms.Resize([256, 256]),
        transforms.CenterCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
CLASS_NAMES = {0: 'Bed', 1: 'Chair', 2: 'Sofa'}
MODEL_RESNET = models.resnet50(pretrained=True)
MODEL_RESNET.fc = nn.Linear(MODEL_RESNET.fc.in_features, 3)
MODEL_RESNET.load_state_dict(torch.load('model_resnet50.pt'))
MODEL_RESNET.eval()

app = Flask(__name__)
app.secret_key = "secret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict(image_path):
    image_data = Image.open(image_path)
    image_transformed = torch.unsqueeze(DATA_TRANSFORMS(image_data), 0)   
    outputs = MODEL_RESNET(image_transformed)
    _, preds = torch.max(outputs, 1)
    return CLASS_NAMES[preds.item()]

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        prediction = predict(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('upload.html', filename=filename, prediction=prediction)
    else:
        flash('Allowed image types are -> jpg, jpeg')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)