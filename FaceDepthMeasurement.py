import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import os
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
import pyttsx3
import tkinter as tk
from tkinter import messagebox
dd0 = 0
dd1 = 0
dd2 = 0


def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def shutdown_system():
    # Use the appropriate command based on the operating system
    if os.name == 'posix':  # Linux, Unix, macOS
        os.system('sudo shutdown now')
    elif os.name == 'nt':   # Windows
        print("Windows does not require sudo permission to shutdown.")
        os.system('shutdown /s /t 1')  # /s for shutdown, /t for time (1 second)
    else:
        print("Unsupported operating system.")

def confirm_shutdown():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Show confirmation dialog box
    confirmed = messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown the system?")

    # If user confirms, shutdown the system
    if confirmed:
        shutdown_system()

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # Drawing
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # # Finding the Focal Length
        # d = 50
        # f = (w*d)/W
        # print(f)

        # Finding distance
        f = 840
        d = (W * f) / w
        print(d)

        if d < 90:

            dd0 += 1

            if dd0 == 20:
                dd0 = 0

                text_to_speech("You are close to moniter!")


        elif d >= 100 and 120 <= d:
            dd0 += 1

            if dd0 == 20:
                dd0 = 0

                text_to_speech("you are in Long Distance from moniter!")


        dd2 += 1

        print(dd2)

        if dd2 == 200:
            dd2 = 0
            text_to_speech("you are in Long time Use")
            root = tk.Tk()
            root.withdraw()  # Hide the root window

            # Show confirmation dialog box
            confirmed = messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown the system?")

            # If user confirms, shutdown the system
            if confirmed:
                shutdown_system()

        cvzone.putTextRect(img, f'Distance: {int(d)}cm',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)

    else:
        dd2 = 0

    cv2.imshow("Image", img)
    cv2.waitKey(1)
