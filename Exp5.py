 !pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
blur = cv2.GaussianBlur(img, (5,5), 0)

kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpened = cv2.filter2D(img, -1, kernel)

show(blur, "Smoothed Image")
show(sharpened, "Sharpened Image")