'''import cv2
import numpy as np

ori = cv2.imread('guardian_heat_11zon.png')
im = cv2.imread("guardian_heat_11zon.png", cv2.IMREAD_GRAYSCALE)

detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(im)

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Original',ori) 
cv2.imshow('BLOB',im_with_keypoints)

for kp in keypoints:
    x,y = kp.pt
    r = kp.size/2
    print(f"Blob at ({x:.2f},{y:.2f}), radius={r:.2f}")

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()'''
import cv2
import numpy as np

ori = cv2.imread('guardian_heat_11zon.png')
im = cv2.imread("guardian_heat_11zon.png", cv2.IMREAD_GRAYSCALE)

detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(im)

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Original',ori) 
cv2.imshow('BLOB',im_with_keypoints)

# Adjust the y-coordinate of the image location by adding an offset of 22 pixels
x_offset = 0
y_offset = 22
cv2.moveWindow('BLOB', x_offset, y_offset)

for kp in keypoints:
    x,y = kp.pt
    r = kp.size/2
    print(f"Blob at ({x:.2f},{y:.2f}), Radius={r:.2f}")

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

