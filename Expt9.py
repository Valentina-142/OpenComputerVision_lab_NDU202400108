 !pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
show(thresh, "Threshold Segmentation")

Z = img.reshape((-1,3))
Z = np.float32(Z)

_, label, center = cv2.kmeans(Z, 3, None,
    (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
    10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
segmented = center[label.flatten()].reshape(img.shape)

show(segmented, "K-Means Segmentation")