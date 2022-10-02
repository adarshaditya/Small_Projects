import pyautogui as  pg
import time

time.sleep(10)

for i in range(500):
    pg.write("Happy Birthday")
    pg.press("Enter")
    
# print("Pyautogui working")