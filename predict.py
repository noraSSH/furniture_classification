import torch
import torch.nn as nn
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import sys
from PIL import Image

data_transforms = transforms.Compose([
        transforms.Resize([256, 256]),
        transforms.CenterCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
class_names = {0: 'Bed', 1: 'Chair', 2: 'Sofa'}

if __name__ == "__main__":
    image_path = sys.argv[1]
    image_data = Image.open(image_path)
    image_transformed = torch.unsqueeze(data_transforms(image_data), 0)
    
    model_resnet = models.resnet50(pretrained=True)
    num_fc = model_resnet.fc.in_features
    model_resnet.fc = nn.Linear(num_fc, 3)
    model_resnet.load_state_dict(torch.load('model_resnet50.pt'))
    model_resnet.eval()
    
    outputs = model_resnet(image_transformed)
    _, preds = torch.max(outputs, 1)
    print("This item is:", class_names[preds.item()])
