import cv2, os, time, datetime

os.makedirs("alerts", exist_ok=True)

cap = cv2.VideoCapture(0)

ret, f1 = cap.read()
ret, f2 = cap.read()

last = 0

while True:
    diff = cv2.absdiff(f1, f2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    _, th = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)

    cnts,_ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    motion = False

    for c in cnts:
        if cv2.contourArea(c) < 1500:
            continue
        motion = True
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(f1,(x,y),(x+w,y+h),(0,255,0),2)

    if motion and time.time()-last > 5:
        name = datetime.datetime.now().strftime("%H-%M-%S")+".jpg"
        cv2.imwrite("alerts/"+name, f1)
        print("Saved:", name)
        last = time.time()

    cv2.imshow("Surveillance", f1)

    f1 = f2
    ret, f2 = cap.read()

    if cv2.waitKey(10)==27:
        break

cap.release()
cv2.destroyAllWindows()