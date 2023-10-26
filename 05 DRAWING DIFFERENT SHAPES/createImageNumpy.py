import numpy as np  
import cv2

# img=cv2.imread('lena.jpg',-1)
img=np.zeros([512,512,3],np.uint8)

#Here the RGB is followed AS  BGR

#Drawing lines:
#Here there are 5 argument:
#1st argument is the image which needs to be used for drawing
#Second and third are the coordinates of the line travel
#fourth is the color scale in BGR format we know it like in CSS.
#fifth is the thickness value number.
img=cv2.line(img,(0,0),(255,255),(0,0,255),4)
cv2.imshow("NEW IMAGE",img)

#Drawaing an arrowed line:
img=cv2.arrowedLine(img,(0,255),(255,255),(60,200,199),10)
cv2.imshow("Arrowed Line Image",img)


#Drawing Rectangle:
#The coordinates in the rectangle are like in the rectangleposition.png

img=cv2.rectangle(img,(380,0),(510,120),(10,100,100),4)
#If instead of 4 in the thickness, if we give -1 then a rectangle is drawn and filled with the color 
# we gave compeletely.
cv2.imshow("RectangleImage",img)

#Drawing The Circle:
#The arguments consists 1st the position and the second is the radus of the circle.
#third the color and last is to completely fill the shape with the color.
img=cv2.circle(img,(447,63),60,(0,255,0),-1);
cv2.imshow("The Circle IMAGE",img)

#Text on the image.
font=cv2.FONT_HERSHEY_SIMPLEX
#The 1st argument is image,2nd is text which is to be inserted, 3rd is the position
#4th is font variable which is decalred in above line.5th is the font size and 
#6th is the color and 7th is the thickness size.
#8th in the line type
img=cv2.putText(img,'NEW TEXT',(10,500),font,4,(100,200,255),3,cv2.LINE_AA)
cv2.imshow("The text",img);
cv2.waitKey()
cv2.destroyAllWindows()


