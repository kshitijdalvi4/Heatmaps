import cv2
import numpy as np;
ori = cv2.imread('guardian_heat_11zon.png')
im = cv2.imread("guardian_heat_11zon.png", cv2.IMREAD_GRAYSCALE)
detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(im)
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Original',ori) 
cv2.imshow('BLOB',im_with_keypoints)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()