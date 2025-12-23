68!pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('open cv.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.axis('off')