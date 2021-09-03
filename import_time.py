import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("numpy")
install("mouse")
install("pyautogui")

import time
import pyautogui as py
from numpy import random
import mouse





while (True):
	i = 100
	x = random.randint(-i,i)
	y = random.randint(-i,i)
	print (x,y)
	mouse.move(x, y, absolute = False, duration = 0.1)
	time.sleep(0.1)
