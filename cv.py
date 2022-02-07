import cv2

clas_caras = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
clas_ojos = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    caras = clas_caras.detectMultiScale(gray)

    for(x,y,w,h) in caras:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img
        cv2.imshow("hola",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
