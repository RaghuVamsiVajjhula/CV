import cv2

#There are 2 arguments to be passed for the imread method.
#The first argument will be the image and the second argument will be 0,1,-1.(These are the ways in whcih the flags are represented.)

img=cv2.imread('lena.jpg',0)
print(img)
#you can see that there is a matrix appered for printing the image.
#Even u give a wrong path or filename there will not be any error occuring.
newimg=cv2.imread('nophoto.jpg',0)
print(newimg)
#We will get an ouput NONE for the newimg printing as there is no such image found.

#WE HAVE JUST READ OUR IMAGE TILL NOW.

#TO DISPLAY THE IMAGE:
#The 1st argument is the name which we get in the image plate which will appear
#The 2nd argument will be the variable name in which  the image is read.
cv2.imshow('imagePhoto',img)
#We have seen that the image is shown for a milli second and disappered so,
#WE use waitkey to wait for the image which is been displayed.

#cv2.waitkey() or cv2.waitkey(0) using this without any arguments will be showing the image for the moment until we close the window.

cv2.waitKey(1000)
#use destryAll windows in order to Destroy all the windows after the time specified.
#we can even destroy some specific window which we will learn later.

cv2.destroyAllWindows()


#WRITING AN IMAGE:
#The first argument is the name of the file which we are writing(the new image is created, so its name is places here)
#The second argument is the img variable which is storing the image which we are copying our new image from.

#After executing below line we can see that a new .png file has been created and stored in our folder.
cv2.imwrite('Lena_copy.png',img)

