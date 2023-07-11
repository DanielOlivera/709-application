import pickle
import cv2 as cv
import pandas as pd
import numpy as np
import dlib
import imutils
import time  
from AR_calculator import *
from AR_utils import *

with open('modelo_LR_M.pkl', 'rb') as file:
    model = pickle.load(file)

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("D:\VSCnotebook\TPfinal\landmarks.dat")
start_time = time.time()
frame_count = 0

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
        TAG = np.asarray(int(0))       
         
        sample_array = np.vstack((OAR, LBAR, RBAR, NUAR, NDAR, LEAR, REAR, OLAR, ILAR, TAG)) 
        sample_array = sample_array.transpose()
                
        pd.DataFrame(sample_array).to_csv('D:\MCD709\data\\0_709_neutral.csv', mode='a', index=False, header=False)
        #pd.DataFrame(sample_array).to_csv('D:\MCD709\data\\1_709_surprise.csv', mode='a', index=False, header=False)
        #pd.DataFrame(sample_array).to_csv('D:\MCD709\data\\2_709_angry.csv', mode='a', index=False, header=False)
        #pd.DataFrame(sample_array).to_csv('D:\MCD709\data\\3_709_happy.csv', mode='a', index=False, header=False)
        #pd.DataFrame(sample_array).to_csv('D:\MCD709\data\\4_709_sad.csv', mode='a', index=False, header=False)
        #pd.DataFrame(sample_array).to_csv('D:\MCD709\data\\5_709_fear.csv', mode='a', index=False, header=False)
        #pd.DataFrame(sample_array).to_csv('D:\MCD709\data\\6_709_disgust.csv', mode='a', index=False, header=False)
        print(sample_array)
        
        prediction_array = np.vstack((OAR, LBAR, RBAR, NUAR, NDAR, LEAR, REAR, OLAR, ILAR))
        prediction_array = prediction_array.transpose()
        feature_names = ['OAR', 'LBAR', 'RBAR', 'NUAR', 'NDAR', 'LEAR', 'REAR', 'OLAR', 'ILAR']
        prediction_array = pd.DataFrame(prediction_array, columns=feature_names)        
        prediction = model.predict(prediction_array)
        
        if prediction == 0:
            label = "Neutral"
        elif prediction == 1:
            label = "Surprise"
        elif prediction == 2:
            label = "Angry"
            
        cv.putText(frame, label, (frame.shape[1] - 150, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv.LINE_AA)
             
    frame_count += 1
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    cv.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv.imshow("", frame)

    key = cv.waitKey(1)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()
