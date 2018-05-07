import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import numpy as np

def identify(imagelist, folder_path):
    for image in imagelist:
        image_edit = cv2.imread(image.data["File Path"])
        image_edit[850:len(image_edit), 0:len(image_edit[0])]=0
        image_edit=cv2.cvtColor(image_edit, cv2.COLOR_BGR2HSV)
        
        lower_red=np.array([0, 10, 20])
        upper_red=np.array([10, 255, 255])
        mask_red1 = cv2.inRange(image_edit, lower_red, upper_red)
        
        lower_red2=np.array([170, 10, 20])
        upper_red2=np.array([179, 255, 255])
        mask_red2 = cv2.inRange(image_edit, lower_red2, upper_red2)

        mask=cv2.bitwise_or(mask_red1,mask_red2)
        
        cv2.imwrite(
            folder_path + "/" + image.data["Name"][:-4] + "-edit.png", mask
            )
        image.data["Edit Img"]=folder_path + "/" + image.data["Name"][:-4] + "-edit.png"

    return imagelist