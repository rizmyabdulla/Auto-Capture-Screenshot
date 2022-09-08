import pyautogui
import time

i = 1
n = 1
while i < 10000:
    pg = pyautogui.screenshot()
    #this Pics Will Save Your Desktop
    pg = pyautogui.screenshot('screenshot{}.png'.format(n))
    i=i+1
    n=n+1
    time.sleep(10)
