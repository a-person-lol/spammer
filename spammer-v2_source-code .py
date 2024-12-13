from time import sleep
import sys
from pynput.keyboard import Key, Controller
kb = Controller()
words = 'IN CASE OF EMERGENCY, PRESS AND HOLD "s" TO STOP'
for char in words:
        sleep(0.025)
        sys.stdout.write(char)
        sys.stdout.flush()
while True:    


    words = '\n Message you want to spam '
    for char in words:
        sleep(0.025)
        sys.stderr.write(char)
    message = input(": ")        
    times = int(input("No. of times you want to spam it:"))
    sleeptime = float(input ("TIME BETWEEN MESSAGES in sec (recommended 0.125):"))
    words = "It will take around "+str(times*sleeptime)+"s to spam the message(s) and an extra 10s of wait time"
    for char in words:
        sleep(0.025)
        sys.stdout.write(char)
        sys.stdout.flush()        
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
        sleep(sleeptime)
        if keyboard.is_pressed("s"):
          break
    while True:
        kb.type("DONE RETURN TO APP")
        words = "Done, restart (Y for yes and N for no)"
        for char in words:
            sleep(0.025)
            sys.stderr.write(char)

        restart = input("?:")

        
        if restart == "N":
                sys.exit()
        if restart =="Y":
                break

