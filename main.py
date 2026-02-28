'''
Run mainX
uncomment to run mainRX
'''
# import mainRX
print('main initiated')
from machine import Pin, Timer
led = Pin(2, Pin.OUT)
def cb(t):
    led.toggle()

tim = Timer(0, freq=5, mode=Timer.PERIODIC, callback=cb)
