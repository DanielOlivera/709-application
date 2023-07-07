from scipy.spatial import distance

def calculate_OAR(outline):
    A = distance.euclidean(outline[0], outline[1])
    B = distance.euclidean(outline[1], outline[2])
    C = distance.euclidean(outline[2], outline[3])
    D = distance.euclidean(outline[3], outline[4])
    E = distance.euclidean(outline[4], outline[5])
    F = distance.euclidean(outline[5], outline[6])
    G = distance.euclidean(outline[6], outline[7])
    H = distance.euclidean(outline[7], outline[8])
    I = distance.euclidean(outline[8], outline[9])
    J = distance.euclidean(outline[9], outline[10])
    K = distance.euclidean(outline[10], outline[11])
    L = distance.euclidean(outline[11], outline[12])
    M = distance.euclidean(outline[12], outline[13])
    N = distance.euclidean(outline[13], outline[14])
    O = distance.euclidean(outline[14], outline[15])
    P = distance.euclidean(outline[15], outline[16])
    Q = distance.euclidean(outline[0], outline[16])
    oar_aspect_ratio = (A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P)/(16.0*Q)
    oar_aspect_ratio = round(oar_aspect_ratio,4)
    return oar_aspect_ratio

def calculate_LBAR(brow):
    A = distance.euclidean(brow[0], brow[8])
    B = distance.euclidean(brow[1], brow[7])
    C = distance.euclidean(brow[3], brow[6])
    D = distance.euclidean(brow[4], brow[5])
    E = distance.euclidean(brow[0], brow[4])
    lbrow_aspect_ratio = (A+B+C+D)/(4.0*E)
    lbrow_aspect_ratio = round(lbrow_aspect_ratio,4)
    return lbrow_aspect_ratio

def calculate_RBAR(brow):
    A = distance.euclidean(brow[0], brow[8])
    B = distance.euclidean(brow[1], brow[7])
    C = distance.euclidean(brow[3], brow[6])
    D = distance.euclidean(brow[4], brow[5])
    E = distance.euclidean(brow[0], brow[4])
    rbrow_aspect_ratio = (A+B+C+D)/(4.0*E)
    rbrow_aspect_ratio = round(rbrow_aspect_ratio,4)
    return rbrow_aspect_ratio

def calculate_NUAR(noseup):
    A = distance.euclidean(noseup[0], noseup[1])
    B = distance.euclidean(noseup[1], noseup[2])
    C = distance.euclidean(noseup[2], noseup[3])
    D = distance.euclidean(noseup[3], noseup[4])
    E = distance.euclidean(noseup[4], noseup[5])
    F = distance.euclidean(noseup[5], noseup[3])
    noseup_aspect_ratio = (A+B+C+D+E+F)/(6.0*F)
    noseup_aspect_ratio = round(noseup_aspect_ratio,4)
    return noseup_aspect_ratio

def calculate_NDAR(nosedown):
    A = distance.euclidean(nosedown[0], nosedown[1])
    B = distance.euclidean(nosedown[1], nosedown[2])
    C = distance.euclidean(nosedown[2], nosedown[3])
    D = distance.euclidean(nosedown[3], nosedown[4])
    E = distance.euclidean(nosedown[4], nosedown[5])
    F = distance.euclidean(nosedown[5], nosedown[6])
    G = distance.euclidean(nosedown[6], nosedown[7])
    H = distance.euclidean(nosedown[0], nosedown[7])
    I = distance.euclidean(nosedown[0], nosedown[3])
    nose_central = (A+B+C)
    nose_long = (nose_central+H+I)/(3.0)
    nosedown_aspect_ratio = (nose_central+D+E+F+G)/(nose_long)
    nosedown_aspect_ratio = round(nosedown_aspect_ratio,4)
    return nosedown_aspect_ratio

def calculate_LEAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    l_eye_aspect_ratio = (A+B)/(2.0*C)
    l_eye_aspect_ratio = round(l_eye_aspect_ratio,4)
    return l_eye_aspect_ratio

def calculate_REAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    r_eye_aspect_ratio = (A+B)/(2.0*C)
    r_eye_aspect_ratio = round(r_eye_aspect_ratio,4)
    return r_eye_aspect_ratio

def calculate_OLAR(outlip):
    A = distance.euclidean(outlip[1], outlip[10])
    B = distance.euclidean(outlip[2], outlip[9])
    C = distance.euclidean(outlip[3], outlip[7])
    D = distance.euclidean(outlip[4], outlip[6])
    E = distance.euclidean(outlip[0], outlip[5])
    outlips_aspect_ratio = (A+B+C+D)/(4.0*E)
    outlips_aspect_ratio = round(outlips_aspect_ratio,4)
    return outlips_aspect_ratio

def calculate_ILAR(inlip):
    A = distance.euclidean(inlip[1], inlip[7])
    B = distance.euclidean(inlip[2], inlip[6])
    C = distance.euclidean(inlip[3], inlip[5])
    D = distance.euclidean(inlip[0], inlip[4])
    inlips_aspect_ratio = (A+B+C)/(3.0*D)
    inlips_aspect_ratio = round(inlips_aspect_ratio,4)
    return inlips_aspect_ratio