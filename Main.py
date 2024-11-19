

from tkinter import *
import os
from tkinter import filedialog
import cv2
import time

from tkinter import messagebox





def endprogram():
	print ("\nProgram terminated!")
	sys.exit()


def fulltraining():
    import cv2
    import sys

    #cascPath = sys.argv[1]
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #faces = faceCascade.detectMultiScale(gray, 1.1, 4)
        #for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()




def fulltraining1():
    import FaceDepthMeasurement




def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 600
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    main_screen.title("Head Pose Estimation")

    Label(text="Head Pose Estimation", width="300", height="5", font=("Calibri", 16)).pack()


    #Button(text="Face Detection", font=(
        #'Verdana', 15), height="2", width="30", command=fulltraining, highlightcolor="black").pack(side=TOP)

    Label(text="").pack()

    Button(text="Face Distance", font=(
        'Verdana', 15), height="2", width="30", command=fulltraining1, highlightcolor="black").pack(side=TOP)
    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()

