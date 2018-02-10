import numpy as np
from PIL import ImageGrab
from PIL import Image
import cv2

def screen_capture():
    while True:
        raw_screen = ImageGrab.grab((98,300,292,495)).resize((900,900))
        screen = np.array(raw_screen)
        new_screen = process_img(screen)
        cv2.imshow('Window1',new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def process_img(original_image):
    #hsv_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    gray_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    ret, binary_img = cv2.threshold(gray_img, 50, 200,cv2.THRESH_BINARY)
    im, contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
    for c in contours:
        (x,y), radius = cv2.minEnclosingCircle(c)
        (x0,y0), radius0 = cv2.minEnclosingCircle(contours[0])
        if (radius > 10):
            li1 = original_image[int(x0), int(y0)]
            li2 = original_image[int(x), int(y)]
            color = original_image[int(x), int(y)]
            if (isEqualv2(li1, li2)):
                fontColor = (0,255,0)
            else:
                fontColor = (0,0,255)
                
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.circle(original_image, (int(x), int(y)), 2, (127,0,255),2)
            processed_img = cv2.putText(original_image, str(color), (int(y)-15, int(x)-10), font, 0.35, fontColor)
    return processed_img

def isEqual(li1, li2):
      return set(li1)==set(li2)

def isEqualv2(li1, li2):
    if (abs(li1[0]-li2[0]) < 3 and abs(li1[1]-li2[1]) < 3 and abs(li1[2]-li2[2]) < 3):
        return True
    else:
        return False
    
screen_capture()