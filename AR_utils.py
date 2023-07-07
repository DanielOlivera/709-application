import cv2 as cv

def append_OAR(frame, face_landmarks):
    outline = []   
    for n in range(0, 17):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        outline.append((x1, y1))
        next_point = n+1
        if n == 16:
            next_point = 16
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
        cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
    return outline
    
def append_LBAR(frame, face_landmarks):
    left_eye_brow_ratio = []
    for n in range(17, 22):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        left_eye_brow_ratio.append((x1, y1))
        next_point = n+1
        if n == 21:
            next_point = 39      
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
        cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
        if next_point == 39:
            for m in range(36, 40):
                m = 75-m
                x1 = face_landmarks.part(m).x
                y1 = face_landmarks.part(m).y
                left_eye_brow_ratio.append((x1, y1))
                inner_next_point = m-1
                if inner_next_point == 35:
                    inner_next_point = 17
                x2 = face_landmarks.part(inner_next_point).x
                y2 = face_landmarks.part(inner_next_point).y
                cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
                cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
    return left_eye_brow_ratio
    
def append_RBAR(frame, face_landmarks):
    right_eye_brow_ratio = []
    for n in range(22, 27):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        right_eye_brow_ratio.append((x1, y1))
        next_point = n+1
        if n == 26:
            next_point = 45      
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
        cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
        if next_point == 45:
            for m in range(42, 46):
                m = 87-m
                x1 = face_landmarks.part(m).x
                y1 = face_landmarks.part(m).y
                right_eye_brow_ratio.append((x1, y1))
                inner_next_point = m-1
                if inner_next_point == 41:
                    inner_next_point = 22
                x2 = face_landmarks.part(inner_next_point).x
                y2 = face_landmarks.part(inner_next_point).y
                cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
                cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
    return right_eye_brow_ratio
    
def append_NUAR(frame, face_landmarks):
    nose_ratio_up = []
    for n in range(21, 23):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        nose_ratio_up.append((x1, y1))
        next_point = n+1
        if n == 22:
            next_point = 42      
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
        cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
        if next_point == 42:
            m = 42
            o = m-14
            p=28
            q = p+11
            r=39
            s = r-18
            x1 = face_landmarks.part(m).x
            y1 = face_landmarks.part(m).y
            nose_ratio_up.append((x1, y1))
            x2 = face_landmarks.part(o).x
            y2 = face_landmarks.part(o).y
            cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
            cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
            x1 = face_landmarks.part(p).x
            y1 = face_landmarks.part(p).y
            nose_ratio_up.append((x1, y1))
            x2 = face_landmarks.part(q).x
            y2 = face_landmarks.part(q).y
            cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
            cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
            x1 = face_landmarks.part(r).x
            y1 = face_landmarks.part(r).y
            nose_ratio_up.append((x1, y1))
            x2 = face_landmarks.part(s).x
            y2 = face_landmarks.part(s).y
            cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
            cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
            if s == 21:
                t=27
                x1 = face_landmarks.part(t).x
                y1 = face_landmarks.part(t).y
                nose_ratio_up.append((x1, y1))
                u = t+1
                x2 = face_landmarks.part(u).x
                y2 = face_landmarks.part(u).y
                cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
                cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
    return nose_ratio_up
    
def append_NDAR(frame, face_landmarks):
    nose_ratio_Down = []
    for n in range(28, 31):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        nose_ratio_Down.append((x1, y1))
        next_point = n+1
        if n == 30:
            next_point = 33
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
        cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
        if next_point == 33:
            for m in range(31, 36):
                x1 = face_landmarks.part(m).x
                y1 = face_landmarks.part(m).y
                nose_ratio_Down.append((x1, y1))
                bridge_next_point = m+1
                if bridge_next_point == 36:
                    bridge_next_point = 28
                x2 = face_landmarks.part(bridge_next_point).x
                y2 = face_landmarks.part(bridge_next_point).y
                cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
                cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
                if bridge_next_point == 28:
                    p1 = 28
                    x1 = face_landmarks.part(p1).x
                    y1 = face_landmarks.part(p1).y
                    p2 = p1+3 
                    x2 = face_landmarks.part(p2).x
                    y2 = face_landmarks.part(p2).y
                    cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
    return nose_ratio_Down

def append_LEAR(frame, face_landmarks):
    left_eye = []
    for n in range(36, 42):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        left_eye.append((x1, y1))
        next_point = n+1
        if n == 41:
            next_point = 36
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173, 255, 47), 1)
        cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return left_eye

def append_REAR(frame, face_landmarks):
    right_eye = []
    for n in range(42, 48):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        right_eye.append((x1, y1))
        next_point = n+1
        if n == 47:
            next_point = 42
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173, 255, 47), 1)
        cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return right_eye

def append_OLAR(frame, face_landmarks):
    out_lips = []
    for n in range(48, 60):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        out_lips.append((x1, y1))
        next_point = n+1
        if n == 59:
            next_point = 48
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
        cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
    return out_lips
    
def append_ILAR(frame, face_landmarks): 
    in_lips = []
    for n in range(60, 68):
        x1 = face_landmarks.part(n).x
        y1 = face_landmarks.part(n).y
        in_lips.append((x1, y1))
        next_point = n+1
        if n == 67:
            next_point = 60
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv.circle(frame, (x1, y1), 3, (173,255,47), 1)
        cv.line(frame,(x1,y1),(x2,y2),(0,255,0),1)
    return in_lips