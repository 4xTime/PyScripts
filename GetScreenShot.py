from PIL import ImageGrab
import time
import keyboard
import os
import cv2
import numpy as np

DIR = ""+"\\" #Directory for your folder
FolderName = "" #folder name
fname = DIR+FolderName+"/"
format = ".jpg" #photo format ".png" ".jpg"

def CountObject()->int:
	k=0
	for i in os.listdir(fname):
		k=k+1
	return k+1

def search_for_dir()->bool:
	tr_fl = False
	for i in os.listdir(DIR):
		if os.path.isdir(os.path.join(DIR+i)):
			if i == FolderName:
				tr_fl = True
				return tr_fl
			if not os.path.exists(DIR+FolderName):
				os.mkdir(DIR+FolderName)
				if not os.path.exists(DIR+FolderName):
					return tr_fl
				else:
					tr_fl = True
					return tr_fl

def TakeScreenShot(on_off:bool,fname,OBC:int):
	while True:
		if keyboard.is_pressed('alt') or on_off == True:
			on_off = True
			if not on_off==False:
				im = ImageGrab.grab()
				im.save(fname + repr(OBC)+format)
				print("IMG SAVE -> "+ fname + repr(OBC)+format)
				OBC = OBC + 1
				if keyboard.is_pressed('ctrl'):
					on_off = False
				time.sleep(0.30)
		


folder_exist = search_for_dir()
OBC = CountObject()	
if folder_exist == True:
	TakeScreenShot(False,fname,OBC)
else:
	print("Folder is missing")
	print("Folder exist = ",folder_exist)

