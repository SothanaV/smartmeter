import numpy as np
import cv2
import requests

cap = cv2.VideoCapture(0)
ret, frame = cap.read()    
cv2.imwrite('pic.png',frame)

url = "http://localhost:8000/meter/piupload/"
fin = open('pic.png', 'rb')
files = {'file': fin}
try:
	r = requests.post(url, files=files)
	print(r.text)
finally:
	fin.close()