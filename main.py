# USAGE : python main.py
from keras.models import load_model
from time import sleep
from tensorflow.keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import time
import webbrowser
from tkinter import *
import tkinter as tk
from tkinter.constants import DISABLED, NORMAL
from tkinter.ttk import Button, Label
from tkinter import messagebox
import csv
import pandas as pd
class User:
    def __init__(self, name, age, gender, username, password):
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        self.gender = gender

from tkinter import *
Users = []
def welocme_page():
    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('643x484')
    root.configure(background='#6E6E8B')
    root.title('Real Time Emotion')

    def btnClickFunction():
        print(pass1.get())
        root.destroy()
        data = pd.read_csv("Users list.csv")
        data.head()
       # with open('Users list.csv', 'r') as file:
        #    reader = csv.reader(file)
         #   for row in reader:
                #if col[2] == Username1.get() and col[3] == pass1.get():
          #      print(row)
            #else:
             #   messagebox.showerror("Title", "Message")
              #  root.destroy()
               # welocme_page()
        #emotion_detect()



    # This is the section of code which creates the a label
    Label(root, text='Welcome, home! ', bg='#A2A2CD', font=('courier', 20, 'bold')).place(x=201, y=34)

    Label(root, text='Username:', bg='#F0F0F8', font=('arial', 12, 'normal')).place(x=152, y=237)

    Label(root, text='Password: ', bg='#F0F0F8', font=('arial', 12, 'normal')).place(x=152, y=277)

    # This is the section of code which creates a text input box
    Username1 = StringVar()
    Username1 = Entry(root, textvariable=Username1)
    Username1.place(x=242, y=237)

    pass1 = StringVar()
    pass1 = Entry(root, textvariable=pass1)
    pass1.place(x=242, y=277)

    # This is the section of code which creates a button
    Button(root, text='Login', bg='#4A4A70', font=('arial', 12, 'normal'), command=lambda : emotion_detect()).place(x=282, y=327)

    Button(root, text='Create New Account', bg='#535386', font=('arial', 12, 'normal'), command=lambda : signup_page()).place(x=232, y=377)
    root.mainloop()

def signup_page():
    root = Tk()

    # this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
    def getCheckboxValue():
        checkedOrNot = cbVariable.get()
        return checkedOrNot

    # this is the declaration of the variable associated with the checkbox
    cbVariable = tk.IntVar()

    # This is the section of code which creates the main window
    root.geometry('580x463')
    root.configure(background='#F0F8FF')
    root.title('Sign up')

    # This is the section of code which creates the a label
    Label(root, text='Create a New Account', bg='#F0F8FF', font=('arial', 18, 'normal')).place(x=172, y=34)

    Label(root, text='Name:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=160, y=102)

    Label(root, text='Age:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=160, y=142)

    Label(root, text='Username:  ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=117, y=182)

    Label(root, text='Password:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=120, y=219)

    Label(root, text='Gender:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=134, y=275)

    # This is the section of code which creates a text input box
    name = StringVar()
    name = Entry(root, textvariable=name)
    name.place(x=229, y=102)

    age = StringVar()
    age = Entry(root, textvariable=age)
    age.place(x=229, y=142)

    username = StringVar()
    username = Entry(root, textvariable=username)
    username.place(x=229, y=182)

    password = StringVar()
    password = Entry(root, textvariable=password)
    password.place(x=229, y=221)

    gender = StringVar()
    gender = Entry(root, textvariable=gender)
    gender.place(x=229, y=275)

    def babo():
        a = User(name.get(), age.get(), gender.get(), username.get(), password.get())
        Users.append(a)
        with open('Users list.csv', 'w') as filehandle:
            for items in Users:
                filehandle.write('%s,' % items.name)
                filehandle.write('%s,' % items.age)
                filehandle.write('%s,' % items.username)
                filehandle.write('%s,' % items.password)
                filehandle.write('%s,' % items.gender)
                print(items.username)
                print(items.password)
            print("File written")
        filehandle.close()

    def isChecked():
        if cb.get() == 1:
            btn['state'] = 'NORMAL'
        elif cb.get() == 0:
            btn['state'] = 'DISABLED'
        else:
            messagebox.showerror('PythonGuides', 'Something went wrong!')

    cb = IntVar()

    # This is the section of code which creates a checkbox
    CheckBoxOne = Checkbutton(root, text='I agree to terms & conditions', variable=cbVariable, bg='#F0F8FF',
                              font=('arial', 12, 'normal'))
    CheckBoxOne.place(x=164, y=331)

    # This is the section of code which creates a button
    btn = Button(root, text='Sign Up!', bg='#F0F8FF', font=('arial', 16, 'normal'), command=lambda: babo()).place(x=213,
                                                                                                                  y=392)

    root.mainloop()

def push_csv():
    with open('Users list.csv', 'w') as filehandle:
        for items in Users:
            filehandle.write('%s\n' % items.name)
        print("File written")
    filehandle.close()
    print('clicked')


def emotion_detect():
    root = Tk()
    face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    classifier = load_model('./Emotion_Detection (1).h5')

    class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprised']

    cap = cv2.VideoCapture(0)
    counter_H = 0
    counter_A = 0
    counter_S = 0
    while True:
        ret, frame = cap.read()

        labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            center_coordinates = x + w // 2, y + h // 2
            radius = h // 2
            cv2.circle(frame, center_coordinates, radius, (0, 0, 100), 3)
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                #mainWindow()
                time.sleep(0.2)

                preds = classifier.predict(roi)[0]
                print("\nprediction = ", preds)
                label = class_labels[preds.argmax()]
                print("\nprediction max = ", preds.argmax())
                print("\nYou are  ", label)
                label_position = (x, y)

                current = label

                if current == 'Happy':
                    counter_H += 1
                    print(counter_H)
                    if counter_H == 5:
                        counter_H = 0
                        def Continue():
                            webbrowser.open_new_tab('https://youtu.be/nxoCIQ469ms')
                        def cancel():
                            root.destroy()

                        # This is the section of code which creates the main window
                        root.geometry('439x304')
                        root.configure(background='#F0F8FF')
                        root.title('Hello, I\'m the main window')

                        # This is the section of code which creates the a label
                        Label(root, text='I guess you\'re happy!', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=132, y=34)
                        Label(root, text='Let\'s play some great music', bg='#F0F8FF',font=('arial', 14, 'normal')).place(x=96, y=121)

                        # This is the section of code which creates a button
                        Button(root, text='Continue', bg='#83838B', font=('arial', 14, 'normal'),command=lambda :Continue()).place(x=71, y=240)
                        Button(root, text='Cancel', bg='#8B8878', font=('arial', 14, 'normal'),command=lambda :cancel()).place(x=272, y=237)

                        root.mainloop()
                if current == 'Sad':
                    counter_S += 1
                    print(counter_S)
                    if counter_S == 5:
                        counter_S = 0
                        def Continue():
                            webbrowser.open_new_tab('https://youtu.be/pxCWiYFkvTg')
                        def cancel():
                            root.destroy()

                        # This is the section of code which creates the main window
                        root.geometry('439x304')
                        root.configure(background='#F0F8FF')
                        root.title('Hello, I\'m the main window')

                        # This is the section of code which creates the a label
                        Label(root, text='I guess you\'re pretty sad!', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=132, y=34)
                        Label(root, text='I can get you out of the mood', bg='#F0F8FF',font=('arial', 14, 'normal')).place(x=96, y=121)

                        # This is the section of code which creates a button
                        Button(root, text='Continue', bg='#83838B', font=('arial', 14, 'normal'),command=lambda :Continue()).place(x=71, y=240)
                        Button(root, text='Cancel', bg='#8B8878', font=('arial', 14, 'normal'),command=lambda :cancel()).place(x=272, y=237)

                        root.mainloop()
                if current == 'Angry':
                    counter_A += 1
                    print(counter_A)
                    if counter_A == 5:
                        counter_A = 0
                        def Continue():
                            webbrowser.open_new_tab('https://youtu.be/Jy5o66NXgVs')
                        def cancel():
                            root.destroy()

                        # This is the section of code which creates the main window
                        root.geometry('439x304')
                        root.configure(background='#F0F8FF')
                        root.title('Hello, I\'m the main window')

                        # This is the section of code which creates the a label
                        Label(root, text='Why are you angry tho?', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=132, y=34)
                        Label(root, text='I will play you some relaxing songs', bg='#F0F8FF',font=('arial', 14, 'normal')).place(x=96, y=121)

                        # This is the section of code which creates a button
                        Button(root, text='Continue', bg='#83838B', font=('arial', 14, 'normal'),command=lambda:Continue()).place(x=71, y=240)
                        Button(root, text='Cancel', bg='#8B8878', font=('arial', 14, 'normal'),command=lambda:cancel()).place(x=272, y=237)
                        val = input("\nType Y to be redirected or press any key to cancel: ")

                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            else:
                cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            print("\n\n")
            cv2.imshow('Emotion Detector', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

welocme_page()
#emotion_detect()
