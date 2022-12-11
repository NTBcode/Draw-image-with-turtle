import turtle
import numpy as np
import cv2

img_source = cv2.imread('/home/binh/Pictures/ronaldo.jpg')
img_source1 = cv2.resize(img_source, (315,390))
img = cv2.flip(img_source1,1)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # chuyển ảnh xám thành ảnh grayscale
thresh = cv2.Canny(img_gray, threshold1=100, threshold2=200) # tìm cạnh của vật thể trong ảnh
contours, w = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for a in range(len(contours)):
	contours_list = contours[a]
	turtle.penup()
	for contours_list2 in contours_list:
		for a, b in contours_list2:
			x = 683/2 - a
			y = 384/2 - b
			turtle.goto(x,y)
			turtle.pendown()
		#print(contours_list2)
			
turtle.mainloop()
