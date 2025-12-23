 !pip install opencv-python opencv-contrib-python
from google.colab import files
files.upload()
kernel = np.ones((5,5), np.float32) / 25
filtered = cv2.filter2D(img, -1, kernel)

motion = np.zeros((15,15))
motion[7,:] = 1/15
motion_blur = cv2.filter2D(img, -1, motion)

show(filtered, "Filtered Image")
show(motion_blur, "Motion Blur")