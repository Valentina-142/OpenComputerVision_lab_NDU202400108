 !pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.hist(gray.ravel(), 256)
plt.title("Histogram")
plt.show()

equalized = cv2.equalizeHist(gray)
show(equalized, "Histogram Equalized Image")