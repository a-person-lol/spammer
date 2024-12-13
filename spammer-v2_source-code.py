from time import sleep
import sys
import keyboard
from pynput.keyboard import Key, Controller
kb = Controller()
words = 'IN CASE OF EMERGENCY, PRESS AND HOLD "s" TO STOP\n Message you want to spam. To operate simply click on textbox where the text is to be typed. '
for char in words:
        sleep(0.025)
        sys.stderr.write(char)
while True:    



    message = input(":")
    times = int(input("No. of times you want to spam it:"))
    words = "It will take around "+str(times*0.125)+"s to spam the message(s) and an extra 10s of wait time"
    for char in words:
        sleep(0.025)
        sys.stderr.write(char)
    x = 10
    print("\n")
    for i in range(0,10):
        x = str(x)
        print("Starting in " + x)
        sleep(1)
        x = int(x)
        x = x-1
   
    for i in range(times):
        kb.type(message)
        kb.tap(Key.enter)
        sleep(0.125)
        if keyboard.is_pressed("s"):
          break
    while True:
        words = "Done, restart (Y for yes and N for no)"
        for char in words:
            sleep(0.025)
            sys.stderr.write(char)

        restart = input("?:")

        
        if restart == "N":
                sys.exit()
        if restart =="Y":
                break

