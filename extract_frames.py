# Importing all necessary libraries 
import cv2 
import os 
import sys
# Read the video from specified path 
cam = cv2.VideoCapture(sys.argv[1]) 
print(sys.argv[1])
try: 
    # creating a folder named data 
    if not os.path.exists('frames'): 
        os.makedirs('frames')
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
# frame 
currentframe = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = './frames/' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 