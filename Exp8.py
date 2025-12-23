 !pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
kernel = cv2.getGaborKernel((21,21), 5, 0, 10, 0.5, 0)
gabor = cv2.filter2D(gray, cv2.CV_8UC3, kernel)

show(gabor, "Gabor Texture Segmentation")