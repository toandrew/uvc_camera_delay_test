import cv2
import sys
import time
import os
import datetime

print('Begin ... ')
capture_width  = 1280
capture_height = 720

cap = cv2.VideoCapture(1)
print('set resolution width: %d' % capture_width)
cap.set(3, capture_width)
print('set resolution height: %d ' % capture_height)
cap.set(4, capture_height)

path = './pics/'
print('Capture in loop ... saved in %s ...' % path)

if not os.path.exists(path):
  os.makedirs(path)

num = 0
while(1):
    ret, frame = cap.read()

    num++
    if num >= 10:
      num = 0
      file_name = './pics/' + str(round(time.time() * 1000)) + '.jpg'
      #print('read!ret:%d, file_name: %s', ret, file_name)

      cv2.imwrite(file_name, frame)

    # to show
    #cv2.imshow("capture", frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #break
cap.release()
#cv2.destroyAllWindows()
