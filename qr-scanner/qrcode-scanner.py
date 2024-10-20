import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cam.isOpened():
    print("Error: Camera failed to open. Please check camera permissions.")
    exit()

cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera:
    success, frame = cam.read()
    
    if not success:
        print("Error: Failed to capture frame.")
        break
    
    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(6)
    
    cv2.imshow("OurQr_Code_Scanner", frame)
    cv2.waitKey(3)
