import numpy as np
import cv2

# Load an image and resize it
img = cv2.imread('./demo.jpg')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Use the goodFeaturesToTrack function to detect corners in the image
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# Convert the corners array to integers
corners = np.int0(corners)

# Draw circles around each detected corner
for corner in corners:
    # print(corner)
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 20, (255, 0, 0), -1)

# Draw lines connecting pairs of corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        # print(corners[i])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

# Create a named window and adjust the window size
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 800, 600)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
