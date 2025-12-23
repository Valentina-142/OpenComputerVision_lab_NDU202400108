 !pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
edges = cv2.Canny(gray, 100, 200)
show(edges, "Canny Edge Detection")