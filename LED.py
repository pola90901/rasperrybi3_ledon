import RPi.GPIO as GPIO
import time



from tkinter import *
window = Tk()

window.title('LED on raspberry')
window.geometry("500x250")



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

# While loop
def ON_func():
        # set GPIO14 pin to HIGH
        GPIO.output(14,GPIO.HIGH)
        # show message to Terminal
        print ("LED is ON")
        

def OFF_func():
        # set GPIO14 pin to HIGH
        GPIO.output(14,GPIO.LOW)
        # show message to Terminal
        print ("LED is OFF")
       
button_on = Button(window,text = "LED ON",command = ON_func)
button_on.place(x = 200, y = 150)

button_off = Button(window,text = "LED OFF",command = OFF_func)
button_off.place(x = 300, y = 150)

window.mainloop()