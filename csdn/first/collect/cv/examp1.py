# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:51:33 2020

@author: 87875
"""

# Python program to explain cv2.imshow() method  
  
# importing cv2  
import cv2  
  
# path  
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'
  
# Reading an image in default mode 
image = cv2.imread(path) 
  
# Window name in which image is displayed 
window_name = 'image'
  
# Using cv2.imshow() method  
# Displaying the image  
cv2.imshow(window_name, image) 
  
#waits for user to press any key  
#(this is necessary to avoid Python kernel form crashing) 
cv2.waitkey(0)  
  
#closing all open windows  
cv2.destroyAllWindows()  