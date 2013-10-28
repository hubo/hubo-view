import socket
import struct
import cv2.cv as cv
import cv2

# Open viewing window
cv.NamedWindow("w2", cv.CV_WINDOW_AUTOSIZE)


MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    tmp = sock.recv(10240)
#    cv2.imshow("w2", tmp)
#    cv2.waitKey(10)
    print tmp