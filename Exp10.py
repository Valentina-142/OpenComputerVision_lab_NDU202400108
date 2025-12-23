!pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
import cv2
import matplotlib.pyplot as plt

def show(img, title="Image"):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load image
img = cv2.imread('open cv.jpeg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw bounding boxes
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display result
show(img, "Object Detection using Haar Cascade")


!git clone https://github.com/ultralytics/yolov5
%cd yolov5
!pip install -r requirements.txt

!python detect.py --weights yolov5s.pt --source ../open\ cv.jpeg

import matplotlib.pyplot as plt
import cv2

result = cv2.imread('runs/detect/exp/open cv.jpeg')
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

plt.imshow(result)
plt.axis('off')
plt.title("Object Detection using YOLOv5")
plt.show()