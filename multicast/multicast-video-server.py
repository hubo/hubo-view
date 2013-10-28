import socket
import time
import cv2.cv as cv
import cv2

# CV setup 
cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
#capture = cv.CaptureFromCAM(0)
capture = cv2.VideoCapture(0)




MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
i = 0
while True:
    # Get Frame
    f, img = capture.read()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("w1", gray_image)
    cv2.waitKey(10)

    #sock.sendto(str(gray_image), (MCAST_GRP, MCAST_PORT))
    sock.sendto(str(gray_image), (MCAST_GRP, MCAST_PORT))
    print i
    i=i+1
    time.sleep(1)
    
