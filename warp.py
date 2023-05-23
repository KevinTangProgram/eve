from cryptography.fernet import Fernet
import matplotlib.image as mpimg
from decimal import Decimal
import pyautogui as py
import numpy as np
import maskpass
import hashlib
import random
import math
import time
import cv2
import os

def password():
	password = ""
	while (True):
		try:
			os.system('cls')
			print("Eve Autopilot 2.0\n")
			password = maskpass.advpass(prompt="Enter the password: ", mask="\u00B7") + "Adamastor"
			if (hashlib.sha256(password.encode('utf-8')).hexdigest() == "559f1112003dcde49fb59dfee6d839c80344f58131861f22ac9763e9899996fa"):
				break
			else:
				os.system('cls')
				maskpass.askpass(prompt="Eve Autopilot 2.0\n\nPress enter to try again.", mask="")
		except:
			os.system('cls')
			maskpass.askpass(prompt="Eve Autopilot 2.0\n\nPress enter to try again.", mask="")

	os.system('cls')
	# password += "Weathered"
	# password = hashlib.sha256(password.encode('utf-8')).hexdigest()
	# password = password[:-21] + '='
	# fernet = Fernet(password)
	#print(fernet.decrypt(b'gAAAAABjGGaQxaEUEWXzYCuPmgYqJrN_rNervKZ7777nRCMkZeI00mf7daE6kem6WW3rvlWylnDzVs74oH1Ums3lh4U5cmBctLzOhf4M8CMAUkxvIkceEssagaIg__itvE4y7VL8KlCi').decode())
	#print(fernet.decrypt(b'gAAAAABjGGa7MZ-BfCTy_lQEQJxxPfbFLfvNrJOa4etdPTxUr0ZxocG6qiuCSY1IuyOXbVGwJ9oB7doW0IikfVzDRfvnlKvcXwL5VO4IKkS44eo6GZmXbXw=').decode())
	#print(fernet.decrypt(b'gAAAAABjGGSz0wzgZUtaISoUAhj-cVrA8HMyBEmvnS1INexXrFYTBLpo1QVSwIX1sfEMeXsyDdarYVO3v2DIdJqQWhJMoYxBbvxbz3NOi_xdqegahZPdybY=').decode())
	#print(fernet.decrypt(b'gAAAAABjGGUKGDVT9jMaHZDI-Nvt3AYrrkGvlPI2Gp7acI3Vks_2qCZjGM0pLRkSnossQdvDIvV3Lhm1aTuvEeDC-bcHd4otkWUUquWaKn_WZWkO01jTngE=').decode())
	#print(fernet.decrypt(b'gAAAAABjGGWKxWaZ4D42LVUvgHK3USxlP7nCQwtAPenEvUzPYXMInOM-z1XoHVfDIl-BYc1dyEyx09_XkPHnB3enBfD5Ip-CQDmQg7TsF6Vdpzbhy7IOGm-i0MKOINl5i63HwS160eog').decode())
	#print(fernet.decrypt(b'gAAAAABjGGXGPMN2Rba1Y8e7KDkjEaCEr2--sIdK7B1WVLS4fCpbSuBEbGEDg-ny3qHqva5H3gDI41ZhSVlRPr1s3A82h_YmHeJoUg97iBp1qqzKhS5a3MBrHEF1L5h3eIuTJ0QCalBH').decode())
	#print(fernet.decrypt(b'gAAAAABjGGY7yTCJJRMzPIRMawDAFRF-evMtC2ne6PmJ-Jf9aOya3GrXNYHY_C3PxWkKTmkB2tDRabKeplN-ATJMfBhS_HEMXVDGjfroMnklNZzgj065PTw=').decode())
	exitCode = False
	try:
		key = maskpass.askpass(prompt="\nPress enter to begin the program.", mask="") + "Warp"
		if (hashlib.sha256(key.encode('utf-8')).hexdigest() == "39865892e074fb33d5505fe64ab05b695ffeb9f142f7eb84d0c869b4c8779668"):
			key += "Spring"
			key = hashlib.sha256(key.encode('utf-8')).hexdigest()
			key = key[:-21] + '='
			fernet = Fernet(key)
			key = fernet.decrypt(b'gAAAAABi4wdn6UEOXcY9gE-ET_xg-lJhbOSw6YG3SaVSucOOZavoPQfj4pAGLaaYAg4ZvTmHvCis0lCTS4U4_9iTS9Vd2_MKl8cq42W8Un5osJX7jR9LS8VvGNa8GHMNH090SVuU3rL-').decode()
			print(key)
			exitCode = True
			#print("\n\nPress enter to close the program.", end = "")
			#maskpass.askpass(prompt="", mask="")
	except:
		pass
	if (exitCode):
		exit()
	
	
def startup():
	print("\n\nProgram started on", time.ctime(time.time()))
	py.hotkey('alt', 'tab')
	time.sleep(1)

def imageProcessor(picture):
	red = picture[..., 0]
	green = picture[..., 1]
	blue = picture[..., 2]
	convertToBlack = (red < 0.70) | (green < 0.70) | (blue < 0.70)
	#convertToWhite = (red < 0.80) | (red > 0.92) |(green < 0.80) | (green > 0.90) | (blue < 0.80) | (blue > 0.90)
	#convertToWhite = (red < 0.90) | (green < 0.87) | (green > 0.88) | (blue < 0.87) | (blue > 0.88)
	picture[convertToBlack] = 0
	convertToWhite = (red != 0) & (green != 0) & (blue != 0)
	picture[convertToWhite] = 1
	return picture

def checkInformation():
	screenshot = py.screenshot(region=(1650, 110, 20, 20))
	screenshot.save('unprocessedInformation.png')
	
	information = mpimg.imread('unprocessedInformation.png')
	mpimg.imsave("processedInformation.png", imageProcessor(information))
	img_rgb = cv2.imread('processedInformation.png')
	template = cv2.imread('i_symbol.png', 0)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.9999
	loc = np.where(res >= threshold)
	lists = loc[1].tolist()
	if (len(lists) > 0):
		return True
	return False

def checkDocking():
	screenshot = py.screenshot(region=(1835, 255, 20, 20))
	screenshot.save('unprocessedDots.png')
	
	information = mpimg.imread('unprocessedDots.png')
	mpimg.imsave("processedDots.png", imageProcessor(information))
	img_rgb = cv2.imread('processedDots.png')
	template = cv2.imread('dots.png', 0)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.9999
	loc = np.where(res >= threshold)
	lists = loc[1].tolist()
	if (len(lists) > 0):
		return True
	return False

def main():
	password()
	startup()
	while (True):
		#get the current time in seconds
		startTime = time.time()
		while (checkInformation()):
			if (time.time() - startTime > 60):
				break
		while (not checkInformation()):
			if (time.time() - startTime > 60):
				break
		if (checkDocking()):
			print("\n\nProgram terminated on", time.ctime(time.time()))
			py.hotkey('alt', 'tab')
			time.sleep(1)
			break
		time.sleep(random.gauss(5.23, 0.875))
		py.click()

def test():
	startup()
	if (checkDocking()):
		print("True")
	startup()

main()
#test()