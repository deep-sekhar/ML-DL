import cv2

img = cv2.imread('./demo.jpg', 1)
# cv2.IMREAD_COLOR (or 1): This loads the image in color format (BGR).
# cv2.IMREAD_GRAYSCALE (or 0): This loads the image in grayscale format.
# cv2.IMREAD_UNCHANGED (or -1): This loads the image as is, including the alpha channel if it exists.
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()