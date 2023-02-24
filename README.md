# Simple Flask application for furniture image classfication using CNN model

Created on: 2023.02.22

**Background:**
This project aims at performing classification tasks on furniture images with target classes of [bed, chair, sofa] using a given dataset of 300 images, as well as implementing a user-friendly API for users to access this prediction functionality.  

## Table of Contents

- [Description](#description)
- [Installation](#installation)
  - [Docker](#Docker)
  - [Terminal](#terminal)
- [Usage](#usage)

## Description

The application deploys a Deep Learning model which utilizes the transfer learning functionality of PyTorch framework. It combines the feature extrator of ResNet50 from torch.models with a customized fully-connected layer to perform the final classification. The model achieves a high validation accuracy of 97.78% on the validation set.

To provide users access to the model, the application provides two API: 1. users can get prediction result by running a Python script; 2. users can run a Flask application, upload an image and then get the predict result. Detailed instructions could be found in [Installation](#installation)

The project implements CI/CD pipeline using Github Action which enables the building of Docker images everytime a push or pull request happens. This effectively increases the working efficiency for this project.

 - app.py: the Flask application
 - Dockerfile: Docker config file
 - model.ipynb: the jupyter notebook to train & output the CNN model
 - model_resnet50.pt: the CNN model used for image classification
 - predict.py: the Python script used for predicting the class of given image
 - requirements.txt: records of dependencies
 - templates/: stores the html files for rendering in the Flask application
 - static/uploads: stores the uploaded images

## Installation
### Docker
_Note: the stable version of Docker image is: norassh98/norarepo:v0.6
To run the application through Docker, you can run the following commands on your terminal:
```markdown
  docker image pull norassh98/norarepo:v0.6
  docker run -it -p 5000:5000 norassh98/norarepo:v0.6
```
Make sure Docker is installed on your machine.

### Terminal
You can also run python app.py to start the application if your environment satisfies the dependencies in requirements.txt.

To run predict.py, make sure that your environment satisfies the dependencies in requirements.txt. This script outputs prediction on a single image in the terminal with the following command:
```markdown
  python predict.py *path_to_image*
```

## Usage
_Note: as the CNN model is quite large (exceeding 90M), the setup and running speed might be slow. Please be patient with the application.

The main page of the Flask application has an upload input form and a submit button. Click on "Choose File" to choose the image you want to test:
![Alt text](img/First.PNG?raw=true "main page")

![Alt text](img/Second.PNG?raw=true "upload image")

After the image is uploaded, click on "Submit" and wait for the application to analyze the results.
![Alt text](img/Third.PNG?raw=true "submit the image for analysis")

Here comes the result!
![Alt text](img/Four.PNG?raw=true "Result!")
