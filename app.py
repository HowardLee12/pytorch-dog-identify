from flask import Flask, request, jsonify
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import requests

app = Flask(__name__)

# 載入預訓練模型
model = models.resnet18(pretrained=True)
model.eval()

# 圖片轉換流程
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

# 下載 ImageNet 標籤
labels_url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels = requests.get(labels_url).text.strip().split("\n")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(file.stream)
    img_t = transform(image).unsqueeze(0)
    out = model(img_t)
    _, index = torch.max(out, 1)
    return jsonify({'prediction': labels[index]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)