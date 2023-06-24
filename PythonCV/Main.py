### OCR ( Optical Character Recognition )

import numpy as np 
import cv2 # OpenCV lib
import easyocr # OCR lib


reader = easyocr.Reader(["en"])
ocrResults = reader.readtext("PythonCV/images/download.jpg")


print(ocrResults)


topLeft = ocrResults[0][0][0]
bottomRight = ocrResults[0][0][2]

text = ocrResults[0][1]

img = cv2.imread("PythonCV/images/download.jpg")
img = cv2.rectangle(img, topLeft, bottomRight, (0,0,255), 2)
img = cv2.putText(img, text, topLeft, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)


cv2.imshow("img", img)
cv2.waitKey()

img = cv2.imread("PythonCV/images/plates.jpg")
ocrResults = reader.readtext("PythonCV/images/plates.jpg")
print(ocrResults)

confidenceThreshold = 0.2

for detections in ocrResults:
    if detections[2] > confidenceThreshold:
        topLeft = [int(value) for value in detections[0][0]]
        bottomRight = [int(value) for value in detections[0][2]]
        text = detections[1]
        img = cv2.rectangle(img, topLeft, bottomRight, (0,0,255), 2)
        img = cv2.putText(img, text, topLeft, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
        
cv2.imshow("img", img)
cv2.waitKey(0)
