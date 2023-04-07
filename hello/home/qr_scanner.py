import cv2
from django.shortcuts import render
import numpy as np
from pyzbar.pyzbar import decode

def scan_qr(request):
    # initialize the camera
    cap = cv2.VideoCapture(0)
    # set the frame size
    cap.set(3, 640) # set width
    cap.set(4, 480) # set height

    # initialize variables
    scanning = False
    
    while True:
        if scanning:
            # read a frame from the camera
            ret, frame = cap.read()
            # decode QR codes in the frame
            decoded_objs = decode(frame)
            # loop over the detected QR codes
            for obj in decoded_objs:
                # print the QR code data
                print("QR code:", obj.data)

                # draw a rectangle around the QR code
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))
                else:
                    hull = points
                n = len(hull)
                for j in range(0, n):
                    cv2.line(frame, hull[j], hull[(j+1)%n], (255, 0, 0), 3)

            # show the frame
            cv2.imshow("QR code scanner", frame)

        # wait for keypress
        key = cv2.waitKey(1)

        # check if 's' key is pressed to start scanning
        if key == ord('s'):
            scanning = True

        # check if 'q' key is pressed to stop scanning
        if key == ord('q'):
            break

    # release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'scan_qr.html')
