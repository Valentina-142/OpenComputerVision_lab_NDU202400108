!pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
import numpy as np

def show(image, title='Image'):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

img = cv2.imread('open cv.jpeg')
h, w = img.shape[:2]

scaled = cv2.resize(img, None, fx=0.5, fy=0.5)

M = np.float32([[1, 0, 50], [0, 1, 50]])
translated = cv2.warpAffine(img, M, (w, h))

R = cv2.getRotationMatrix2D((w//2, h//2), 45, 1)
rotated = cv2.warpAffine(img, R, (w, h))

show(img, "Original")
show(scaled, "Scaled")
show(translated, "Translated")
show(rotated, "Rotated")