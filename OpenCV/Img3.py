import numpy as np
import cv2

# Capture video from default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    # ret is a boolean value indicating whether or not a frame was successfully read from the video capture device. It will be True if a frame was read successfully, and False otherwise.

    # Get the width and height of the video capture
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Create a new image array of the same shape as the captured frame
    image = np.zeros(frame.shape, np.uint8)

    # Resize the captured frame to half its size
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Copy and rotate the smaller frame to each quadrant of the new image array
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    # Show the new image in a window named "frame"
    cv2.imshow('frame', image)

    # Wait for a key press, and break the loop if the "q" key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and destroy the window
cap.release()
cv2.destroyAllWindows()
