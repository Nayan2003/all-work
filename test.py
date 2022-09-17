import pyautogui as spam
import time

limit =input("Your limit:")
msg=input("enter your massege:")

i = 0


time.sleep(10)

while i<int(limit):
    spam.typewrite(msg)
    spam.press('Enter')

    i+=1