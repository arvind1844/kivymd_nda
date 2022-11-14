import cv2
from PIL import Image
capture = 0
cam_img = 'img1.png'
def open_camera(phone):
    global capture
    
    videoCaptureObject = cv2.VideoCapture(0)
    

    while True:
        ret, frame = videoCaptureObject.read()
        cv2.imshow("Capturing Image", frame)
        cv2.moveWindow("Capturing Image", 430,140)
        cv2.resizeWindow("Capturing Image", 500, 350)

        
        if capture == True:
            capture = 0
            cv2.imwrite("C:/nda_image/" + f'{phone}' + '.png', frame)
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def save_snap():
    global capture
    capture = 1
    
    
