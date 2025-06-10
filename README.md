


# 🐶 PyTorch Dog Classifier API

A simple Flask API using a pre-trained ResNet-18 model (via PyTorch) to identify dog breeds or other objects in uploaded images.

> Upload a photo and get back what the model thinks it is (e.g., golden retriever, tabby cat, sports car...).

---

## 🔧 Installation Guide

This project is intended to be run on a Linux-based environment such as Ubuntu or an EC2 instance.

### 1. Install Python 3 and pip

Ubuntu (20.04+):

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

2. Clone the repository

git clone https://github.com/HowardLee12/pytorch-dog-identify.git
cd pytorch-dog-identify

3. Create and activate a virtual environment

python3 -m venv myenv
source myenv/bin/activate

4. Install Python dependencies

pip install -r requirements.txt

If you don’t have a requirements.txt, you can install manually:

pip install flask torch torchvision pillow requests


⸻

🚀 Run the API Server

python3 app.py

The Flask server will run on:

http://0.0.0.0:5000

Make sure your security group or firewall allows TCP port 5000.

⸻

🧪 How to Use

Send a POST request to /predict with an image file.

Example (using curl):

curl -X POST -F "image=@dog.jpg" http://<your-ec2-public-ip>:5000/predict

Example Response:

{
  "prediction": "golden retriever"
}


⸻

🛠 Tech Stack
	•	Python 3
	•	Flask
	•	PyTorch (ResNet18 pretrained)
	•	TorchVision
	•	Pillow (PIL)

⸻

📦 Project Structure

File	Description
app.py	Main Flask application
requirements.txt	Python dependency list (optional)
dog.jpg	Sample image for testing (optional)


⸻

🧰 Tips
	•	Run the Flask server in the background using tmux, screen, or:

nohup python3 app.py > flask.log 2>&1 &

	•	To stop the app:

ps aux | grep app.py
kill <PID>



⸻

🐾 Sample Output

$ curl -X POST -F "image=@dog.jpg" http://<your-ip>:5000/predict
{"prediction": "golden retriever"}


⸻

📜 License

MIT License

---

這份 `README.md` 適合公開專案，能讓其他人快速上手部署。如果你有後續想用 Docker、接 HTTPS、或上 ECS，我可以幫你補上對應章節。需要嗎？
