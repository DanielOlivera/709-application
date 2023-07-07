import cv2 as cv
import pandas as pd
import numpy as np
import dlib
import imutils
from AR_calculator import *
from AR_utils import *

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("D:\VSCnotebook\TPfinal\landmarks.dat")

while True:
    _, frame = cap.read()
    frame = cv.flip(frame,1)
    frame = imutils.resize(frame, width=640)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = hog_face_detector(gray)
    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)
        
        Outline = []#(0,17)
        left_eye_brow_ratio = []#(17,22 & 36,40)
        right_eye_brow_ratio = []#(22,27 & 42,46)
        NoseratioUp =[]#(21,22,42,28,39,27)
        NoseratioDown = []#(28,29,30,31,32,33,34,35)
        leftEye = []#(36,42)
        rightEye = []#(42,48) 
        outLips = []#(48,60)
        inLips = []#(60,68)
        
        outline = append_OAR(frame, face_landmarks)
        OAR = calculate_OAR(outline)
        OAR = np.asarray(OAR)
        left_eye_brow_ratio = append_LBAR(frame, face_landmarks)
        LBAR = calculate_LBAR(left_eye_brow_ratio)
        LBAR = np.asarray(LBAR)
        right_eye_brow_ratio = append_RBAR(frame, face_landmarks)
        RBAR = calculate_RBAR(right_eye_brow_ratio)
        RBAR = np.asarray(RBAR)
        nose_ratio_up = append_NUAR(frame, face_landmarks)
        NUAR = calculate_NUAR(nose_ratio_up)
        NUAR = np.asarray(NUAR)
        nose_ratio_down = append_NDAR(frame, face_landmarks)
        NDAR = calculate_NDAR(nose_ratio_down)
        NDAR = np.asarray(NDAR)
        left_eye = append_LEAR(frame, face_landmarks)
        LEAR = calculate_LEAR(left_eye)
        LEAR = np.asarray(LEAR)
        right_eye = append_REAR(frame, face_landmarks)
        REAR = calculate_REAR(right_eye)
        REAR = np.asarray(REAR)
        out_lips = append_OLAR(frame, face_landmarks)
        OLAR = calculate_OLAR(out_lips)
        OLAR = np.asarray(OLAR)
        in_lips = append_ILAR(frame, face_landmarks)
        ILAR = calculate_ILAR(in_lips)
        ILAR = np.asarray(ILAR)
        
        sample_array = np.vstack((OAR, LBAR, RBAR, NUAR, NDAR, LEAR, REAR, OLAR, ILAR)) 
        sample_array = sample_array.transpose()
        pd.DataFrame(sample_array).to_csv('D:\MCD709\data\\709_neutral.csv', mode='a', index=False, header=False)
        print(sample_array)

    cv.imshow("", frame)

    key = cv.waitKey(1)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()