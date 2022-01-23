import cv2
import dropbox
import time
import random

startTime = time.time()

def takeSnapshot():
    num = random.randint(0,100)
    videoObject = cv2.VideoCapture(0)
    result = True

    while (result) :
        ret, frame = videoObject.read()
        imageName = str(num) +'img.jpg'
        cv2.imwrite(imageName, frame)
        startTime=time.time

        result = False

    return imageName
    
    videoObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = 'uSrXyGU0_DUAAAAAAAAAAVZU2DYCqzxoNRDayD6cUCX99DIWt9t-lSHlkaxDBcyx'
    file_from = imageName
    file_to = '/Class102/'+ imageName
    dbx = dropbox.Dropbox(access_token)

    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

    print("File uploaded")

def main():
    while (True) :
        if((time.time()-startTime)>=1):
            name = takeSnapshot()
            upload_file(name)

main()


