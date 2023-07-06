import cv2
import dlib
#import paho.mqtt.client as paho
from scipy.spatial import distance
#broker = "127.0.0.1"
#port = 1883
#count1 = 0

def on_publish(client,userdata,result):
    pass

#cliente = paho.Client("control1")
#cliente.on_publish = on_publish
#cliente.connect(broker,port)

def calculate_EAR(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear_aspect_ratio = (A+B)/(2.0*C)
	return ear_aspect_ratio

cap = cv2.VideoCapture(0)
hog_face_detector = dlib.get_frontal_face_detector()
datafile = "D:\VSCnotebook\TPfinal\landmarks.dat"
#dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
dlib_facelandmark = dlib.shape_predictor(datafile)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = hog_face_detector(gray)
    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)
        leftEye = []
        rightEye = []
    for n in range(36,42):
        x = face_landmarks.part(n).x
        y = face_landmarks.part(n).y
        leftEye.append((x,y))
        next_point = n+1
        if n == 41:
            next_point = 36
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

    for n in range(42,48):
        x = face_landmarks.part(n).x
        y = face_landmarks.part(n).y
        rightEye.append((x,y))
        next_point = n+1
        if n == 47:
            next_point = 42
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)
        EAR = (left_ear+right_ear)/2
        EAR = round(EAR,2)
        if EAR > 0.26:
            cv2.putText(frame,"Estado_alerta",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            E1 = 1
            E2 = 0
            E3 = 0
            #cliente.publish("canal1",1)
            #cliente.publish("canal2",0)
            #cliente.publish("canal3",0)
        elif ((EAR<=0.26) and (EAR>=0.21)):
            cv2.putText(frame,"Estado_cansado",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
            E1 = 0
            E2 = 1
            E3 = 0
            #cliente.publish("canal1",0)
            #cliente.publish("canal2",1)
            #cliente.publish("canal3",0)
        elif EAR <= 0.20:
            cv2.putText(frame,"Estado_peligro",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            E1 = 0
            E2 = 0
            E3 = 1
            #cliente.publish("canal1",0)
            #cliente.publish("canal2",0)
            #cliente.publish("canal3",1)

        if ((E1 == 0) and ((E2 == 1) or (E3 == 1))):
            count1 = count1 + 1
            #print("TEST: ", count1)
            #print("Estado de alarma: ", EAR, "ESTADO")
            #cliente.publish("canal4","ALARMA")
            #cliente.publish("canal5",0)
            ##if count1 >= 50:
                #cliente.publish("canal4","ALARMA")
                #cliente.publish("canal5",0)
                #cliente.publish("canal6",0)     
        else:
            count1 = 0
            #cliente.publish("canal4","OK")
            #cliente.publish("canal5",1)
            #cliente.publish("canal6",1)
        	
    cv2.imshow("Panel1", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
	
cap.release()
cv2.destroyAllWindows()