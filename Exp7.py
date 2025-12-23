 !pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
gray_float = np.float32(gray)
dst = cv2.cornerHarris(gray_float, 2, 3, 0.04)

img_harris = img.copy()
img_harris[dst > 0.01 * dst.max()] = [0,0,255]

show(img_harris, "Harris Corners")