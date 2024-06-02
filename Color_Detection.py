import numpy as np
import cv2


def Detect_Color(Lower: np.array, Upper: np.array, Picture_Path):
    
    PICTURE = cv2.imread(f"{Picture_Path}")
    Mask = cv2.inRange(PICTURE, Lower, Upper)

    Contours, _ = cv2.findContours(Mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for key, contour in enumerate(Contours):
        area = cv2.contourArea(contour)
        x,y,w,h = cv2.boundingRect(contour)
        
        imageFrame = cv2.rectangle(PICTURE, (x,y), (x+w, y+h), (255,0,255), 2)

        if area < 100:
            cv2.putText(PICTURE, "Color Detected", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (53,254,250), 1)


    output = cv2.bitwise_and(PICTURE, PICTURE, mask=None)

    cv2.imshow("Color Detection", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()