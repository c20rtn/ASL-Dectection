import cv2
import os
import time
import uuid

IMG_PTH = "images"
labels = ["hello","yes","no","thanks"]

no_imgs = 20

for label in labels:
    dir_path = "images\\" + label

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    print("collecting images for " + label)

    #allow time for capture
    for x in range(0, 5):
        print("We're on time %d" % (x))
        time.sleep(1)

        
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    time.sleep(1)

    for num in range(no_imgs): #collect 20 pics
        ret, frame = cap.read() #get pic
        imgname = os.path.join(IMG_PTH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1()))) #name the image
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(0.5) #time to do new image

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    cap.release()
cv2.destroyAllWindows()