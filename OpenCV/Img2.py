import cv2
import random

img = cv2.imread('./demo.jpg', -1)

# Change first 100 rows to random pixels
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copy part of image
tag = img[400:700, 600:900]
img[100:400, 650:950] = tag

# Create a named window and adjust the window size
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 800, 600)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()