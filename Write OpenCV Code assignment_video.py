''' 2. Record a 10 second video of yourself waving your hand, in grayscale.'''
#reference: https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

import cv2
#import numpy
import time

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if cap.isOpened() == False:
    print('Error opening video stream or file')

# Default resolutions of the frame are obtained.
# The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


fps = 30//2 #Frame Per Second implies 15 picture frames per second, moving fast?

# Define the codec and create VideoWriter object.
# The color and gray outputs are stored in 'gray output.avi' and 'color output' files respectively.

gOut = cv2.VideoWriter('gray output.avi', cv2.VideoWriter_fourcc('M','J', 'P', 'G'), fps, (frame_width, frame_height), 0)
cOut = cv2.VideoWriter('color output.avi', cv2.VideoWriter_fourcc('M','J', 'P', 'G'), fps, (frame_width, frame_height))

startTime = time.time()
while cap.isOpened(): #OR while (True):
    ret, frame = cap.read()
    
    if ret == True:
        #Convert colored frame to gray before writing(or saving)
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Write the frame into the file 'gray output.avi'
        gOut.write(grayFrame)
        cOut.write(frame)


        # Display the resulting frames RGB and Gray    
        cv2.imshow('Frame', frame)
        cv2.imshow('Gray Video', grayFrame)

        framesDelay = 1 #This number is equal to the time in milliseconds we want each frame to be displayed even if we press any key
        
        # Press Q on keyboard to stop recording
        #waitKey actually determines how much time your program "waits" for a key being pressed by the user before going on with the rest of the program.
        #waitkey(0) is used for image which shows indefinitely until designated escape key is presses
        if cv2.waitKey(framesDelay) & 0xFF == ord('q'):
        #With respect to set operations, the & operator is equivalent to the intersection() operation, and creates a new set with elements common to s and t:
            break
        

        
        endTime = time.time()
        elapsed = endTime - startTime
        if elapsed >= 10: #seconds time.time() output seconds
            break
        
        
        

    # Break the loop
    else:
        break
# When everything done, release the video capture and video write objects
cap.release()
gOut.release()
cOut.release()

# Closes all the frames
cv2.destroyAllWindows()