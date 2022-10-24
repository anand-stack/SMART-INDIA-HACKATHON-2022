from base64 import encode
from pydoc import classname
from unicodedata import name
import cv2
import numpy as np
import face_recognition
import os
import pandas as pd
from datetime import datetime
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import multiprocessing
import tkinter as tk
import sys
import os
import pandas as pd
import time
import datetime
from kivymd.uix.label import MDLabel
import subprocess
import pandareading

path = 'C:/Users/asgav/Downloads/face/face/image'
image = []
classNames = []
myList = os.listdir(path)
# print(myList)

for i in myList:
    curImg = cv2.imread(f'{path}/{i}')
    image.append(curImg)
    classNames.append(os.path.splitext(i)[0])


# print(classNames)
def fEncodings(image):
    encolist = []
    for img in image:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encolist.append(encode)
        print(encolist)
    return encolist



encodeListKnown = fEncodings(image)

presentlist = []
presentlist2 = []


# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
'''def relist():
    exel.writting(presentlist)'''


def function():
    a={'VENKAT','KALAM','SRIKANTH','ANAND','SARAN','GAUTHAM','KAVYA','HARIRAM','RAGAVI'}
    b=set()
    z=0
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    f = 1
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faces_cur_frame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, faces_cur_frame)

        for encodeFace, faceLoc in zip(encodesCurFrame, faces_cur_frame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                '''if name not in presentlist2:
                    print(name)
                    presentlist2.append(name)
                    presentlist.append([name, str(datetime.now())])'''
                b.add(name)
                z=z+1

                if z == 10:
                    f = 0
                    break
        if f == 0:
            print(b)
            q=list(b)
            excelheader = ["name"]
            data=[]
            for i in range(0,len(q)):
                r=[]
                r.append(q[i])
                data.append(r)
            df = pd.DataFrame(data, columns=excelheader)
            writer = pd.ExcelWriter('file1.xlsx', engine='xlsxwriter')
            df.to_excel(writer, sheet_name='present')
            writer.save()
            u=list(a-b)
            excelheader = ["name"]
            data=[]
            for i in range(0,len(u)):
                e=[]
                e.append(u[i])
                data.append(e)
            df = pd.DataFrame(data, columns=excelheader)
            writer = pd.ExcelWriter('file2.xlsx', engine='xlsxwriter')
            df.to_excel(writer, sheet_name='present')
            writer.save()

            s= pandareading.pandasfunc()
            print(s)
            excelheader = ["name"]
            data = []
            for i in range(0, len(s)):
                e = []
                e.append(s[i])
                data.append(e)
            df = pd.DataFrame(data, columns=excelheader)
            writer = pd.ExcelWriter('panda.xlsx', engine='xlsxwriter')
            df.to_excel(writer, sheet_name='present')
            writer.save()
            break
        cv2.imshow('Webcam', img)
        cv2.waitKey(1)


if _name_ == '_main_':
    function()
